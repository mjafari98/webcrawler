from bs4 import BeautifulSoup as bs
import json
import requests

def adding(URI, dictionary, depth):
    if depth > 0:
        # Send GET request to take the HTML DOC from the URI
        root_URI = requests.get(URI)

        # Render HTML_DOC from string to beautifulsoup
        soup = bs(root_URI.text, 'html.parser')

        # Query on beautifulsoup to pull out hyperlinks
        for link in soup.find_all('a'):
            if len(str(link.get('href')))>3:
                if str(link.get('href'))[0:4] == 'http' \
                and link.get('href') != None \
                and str(link.get('href')) not in dictionary:
                    dictionary[str(link.get('href'))] = dict()
                    if depth > 1:
                        adding(str(link.get('href')), dictionary[str(link.get('href'))], depth-1)


# The tree of links appends here
tree_of_hyperlinks = dict()

# Root URI that we want to conduct analysis on it
print('Enter the URI:', end=' ')
the_root_URI_input = input()

# Get the depth of analysing
print('Enter the depth:', end=' ')
depth = int(input())

# initialize dictionary
tree_of_hyperlinks[the_root_URI_input] = dict()

# web scraping starts here!
adding(the_root_URI_input, tree_of_hyperlinks[the_root_URI_input], depth)

j = json.dumps(tree_of_hyperlinks, indent=4)
print(j)
