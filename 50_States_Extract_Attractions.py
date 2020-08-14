#parse all 50 state html files
#By: Bradford Stallworth
#MIS 3810 EXTRA CREDIT FINAL COPY

from bs4 import BeautifulSoup
import pandas as pd
import csv

#open csv file that contains lower cased state names
with open('50_us_states_lowercased.csv', newline= '') as f:
    reader = csv.reader(f)
    csv_states = list(reader)

#importing the csv file and creating a list caused a minor issue
# example [[ohio],[florida],[chicago]]
#figured out a way to remove the brackets inside the list by nesting list comprehension

states = []
for sublist in csv_states:
    for val in sublist:
        states.append(val)


alldata = []
for s in states:
    # open HTML page for all 50 states
    with open(s+'-attraction2.html', 'r',encoding = 'utf-8') as file:
        page = file.read()
    soup = BeautifulSoup(page,'html.parser')
    soup.prettify()
    print(soup) #Why is it i take this away and it only prints one line?

    #example: ohio top 20 Attractions
    title = soup.findAll('h1')
    print(title)

    #repeat string
    repeat_title = (title)*10
    
    

    #Paragraphs
    attraction = soup.findAll('h2')
    print(attraction)
 
   

    #address
    results = []
    for strong_tag in soup.findAll('strong'):
        results.append(strong_tag.next_sibling)

    #drop tags
    repeat_title = list(map(lambda x: x.text, repeat_title))
    attraction = list(map(lambda x: x.text, attraction))

    #combine data into a list
    x = list(zip(repeat_title, attraction, results))
    alldata.append(x)

#flatten data
alldata = sum(alldata,[])

# convert into a dataframe and save to file
rows = pd.DataFrame(alldata,columns=['State','Attraction', 'Address' ])
print(rows)
rows.to_csv('all-attractions.txt',sep='\t',index=False)

    
    
