from bs4 import BeautifulSoup
import requests

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
warnings.filterwarnings("ignore", category=UserWarning, module='requests')

# html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

# # Beautiful Soup transforms a complex HTML document into a complex tree of Python objects. 
# # The BeautifulSoup object can create other types of objects
# soup = BeautifulSoup(html, 'html.parser')

# # We can use the method prettify() to display the HTML in the nested structure:
# #print(soup.prettify())

# # We can access the title tag and its content:
# tag_object = soup.title
# print("tag object:",tag_object)

# # We can access the name of the tag, h3:
# tag_object = soup.h3
# print(tag_object)

# # We can access the child tag of h3, which is b:
# tag_child = tag_object.b
# print(tag_child)

# #we can access the parent tag of b, which is h3:
# parent_tag = tag_child.parent
# print(parent_tag)

# # access the parent of parent tag of b, which is bo
# body_tag = parent_tag.parent
# print(body_tag)

# # accessing the next sibling of h3, which is p:
# sibling_1 = parent_tag.next_sibling
# print(sibling_1)

# # accessing the next sibling of p, which is h3:
# sibling_2 = sibling_1.next_sibling
# print(sibling_2)

# #If the tag has attributes, the tag id="boldest" has 
# # an attribute id whose value is boldest. 
# # You can access a tag’s attributes by treating the tag like a dictionary:
# tag_attr = tag_child['id']
# print(tag_attr)

# #accessing the dictionary of attributes:
# tag_attr = tag_child.attrs
# print(tag_attr)

# # accessing the value of attribute id using python get method:
# print(tag_child.get('id'))

# # Beautiful Soup uses the NavigableString class to contain this text. 
# # In our HTML we can obtain the name of the first player by 
# # extracting the sting of the Tag
# tag_string = tag_child.string
# print(tag_string)

# # We can check the type of the object tag_string:
# print(type(tag_string))

# # covert it to sting object in Python from soup NavigableString object:
# str_tag = str(tag_string)
# print(type(str_tag))

# table="<table><tr><td id='flight' >Flight No</td><td>Launch site</td><td>Payload mass</td></tr><tr><td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a> </td><td>80 kg</td></tr></table>"
# table_soup = BeautifulSoup(table, 'html.parser')

# # Extracting all the rows of the table
# table_bs = table_soup.find_all('tr')
# for i,row in enumerate(table_bs):
#     print("row",i)
#     cells=row.find_all('td')
#     for j,cell in enumerate(cells):
#         print('colunm',j,"cell:",cell)

# # Extracting all the rows of the table using id
# table_soup.find_all(id="flight")

# # Extracting all the a tag with href
# list_input=table_soup.find_all(href="https://en.wikipedia.org/wiki/Florida")
# print(list_input)

# print(table_soup.find_all(href=True))  # all a tags with href

# url = "https://web.archive.org/web/20230224123642/https://www.ibm.com/us-en/"

# data  = requests.get(url).text

# soup = BeautifulSoup(data, 'html.parser')

# # Extracting all the a tag with href
# for link in soup.find_all('a',href=True):  
#     print(link.get('href'))


import pandas as pd

#The below url contains html tables with data about world population.
url = "https://en.wikipedia.org/wiki/World_population"

# get the contents of the webpage in text format and store in a variable called data
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4472.124 Safari/537.36"
}

data  = requests.get(url, headers=headers).text

soup = BeautifulSoup(data, 'html.parser')

#find all html tables in the web page
tables = soup.find_all('table') # in html table is represented by the tag <table>
# we can see how many tables were found by checking the length of the tables list
print(len(tables))

for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)

# print(tables[table_index].prettify())

# population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])

# for row in tables[table_index].tbody.find_all("tr"):
#     col = row.find_all("td")
#     if col:
#         rank = col[0].text.strip()
#         country = col[1].text.strip()
#         population = col[2].text.strip()
#         area = col[3].text.strip()
#         density = col[4].text.strip()

#         # Create a temporary DataFrame for the new row
#         new_row = pd.DataFrame([{"Rank": rank, "Country": country, "Population": population, "Area": area, "Density": density}])

#         # Use concat 
#         population_data = pd.concat([population_data, new_row], ignore_index=True)



pd.read_html(str(tables[5]), flavor='bs4')

population_data_read_html = pd.read_html(str(tables[5]), flavor='bs4')[0]

print(population_data_read_html)