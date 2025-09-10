from bs4 import BeautifulSoup
import requests

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
warnings.filterwarnings("ignore", category=UserWarning, module='requests')

html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

# Beautiful Soup transforms a complex HTML document into a complex tree of Python objects. 
# The BeautifulSoup object can create other types of objects
soup = BeautifulSoup(html, 'html.parser')

# We can use the method prettify() to display the HTML in the nested structure:
#print(soup.prettify())

# We can access the title tag and its content:
tag_object = soup.title
print("tag object:",tag_object)

# We can access the name of the tag, h3:
tag_object = soup.h3
print(tag_object)

# We can access the child tag of h3, which is b:
tag_child = tag_object.b
print(tag_child)

#we can access the parent tag of b, which is h3:
parent_tag = tag_child.parent
print(parent_tag)

# access the parent of parent tag of b, which is bo
body_tag = parent_tag.parent
print(body_tag)

# accessing the next sibling of h3, which is p:
sibling_1 = parent_tag.next_sibling
print(sibling_1)

# accessing the next sibling of p, which is h3:
sibling_2 = sibling_1.next_sibling
print(sibling_2)