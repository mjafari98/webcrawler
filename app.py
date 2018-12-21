from bs4 import BeautifulSoup as bs
import requests

# The tree of links appends here
tree_of_hyperlinks = dict()

# Root URI that we want to conduct analysis on it
the_root_URI_input = input()
# Get the depth of analysing
depth = int(input())

# Send GET request to take the HTML DOC from the URI
root_URI = requests.get(the_root_URI_input)

# Render HTML_DOC from string to beautifulsoup
soup = bs(root_URI.text, 'html.parser')
