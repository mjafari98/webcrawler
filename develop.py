from bs4 import BeautifulSoup as bs
import requests

def adding(URI, dictionary, depth):
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
                if depth > 0:
                    adding(str(link.get('href')), dictionary[str(link.get('href'))], depth-1)


# The tree of links appends here
tree_of_hyperlinks = dict()

print('Enter the URI:', end=' ')
# Root URI that we want to conduct analysis on it
the_root_URI_input = input()

print('Enter the depth:', end=' ')
# Get the depth of analysing
depth = int(input())

tree_of_hyperlinks[the_root_URI_input] = dict()

adding(the_root_URI_input, tree_of_hyperlinks[the_root_URI_input], depth)

print(tree_of_hyperlinks)
