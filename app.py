from bs4 import BeautifulSoup as bs
import requests

# The tree of links appends here
tree_of_hyperlinks = dict()

# Root URI that we want to conduct analysis on it
the_root_URI_input = input()
# Get the depth of analysing
# depth = int(input())

# Send GET request to take the HTML DOC from the URI
root_URI = requests.get(the_root_URI_input)

# Render HTML_DOC from string to beautifulsoup
soup = bs(root_URI.text, 'html.parser')

# Query on beautifulsoup to pull out hyperlinks
for link in soup.find_all('a'):
    if str(link.get('href'))[0] != '/' \
    and link.get('href') != None \
    and str(link.get('href')) not in tree_of_hyperlinks:
        tree_of_hyperlinks[str(link.get('href'))] = dict()


# ------------ second step
for link, tree in tree_of_hyperlinks.items():
    # Send GET request to take the HTML DOC from the URI
    root_URI = requests.get(link)

    # Render HTML_DOC from string to beautifulsoup
    soup = bs(root_URI.text, 'html.parser')

    # Query on beautifulsoup to pull out hyperlinks
    for link in soup.find_all('a'):
        if len(str(link.get('href')))>3:
            if str(link.get('href'))[0:4] == 'http' \
            and link.get('href') != None \
            and str(link.get('href')) not in tree \
            and str(link.get('href')) not in tree_of_hyperlinks:
                tree[str(link.get('href'))] = dict()

# ------------ third step
for link, tree in tree_of_hyperlinks.items():
    # Send GET request to take the HTML DOC from the URI
    root_URI = requests.get(link)

    # Render HTML_DOC from string to beautifulsoup
    soup = bs(root_URI.text, 'html.parser')

    # Query on beautifulsoup to pull out hyperlinks
    for link in soup.find_all('a'):
        if len(str(link.get('href')))>3:
            if str(link.get('href'))[0:4] == 'http' \
            and link.get('href') != None \
            and str(link.get('href')) not in tree:
                tree[str(link.get('href'))] = dict()


print(tree_of_hyperlinks)
