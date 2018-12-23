from bs4 import BeautifulSoup as bs
import json
import requests
import re


def adding(URI, dictionary, depth):
    try:
        if depth > 0:
            # Send GET request to take the HTML DOC from the URI
            # root_URI = requests.get(URI)

            root_URI = open(URI, "r")

            # Render HTML_DOC from string to beautifulsoup
            soup = bs(root_URI.read(), 'html.parser')

            # Query on beautifulsoup to pull out hyperlinks
            # for link in soup.findAll('a', attrs={'href': re.compile("^http[s]*://")}):
            # for link in soup.findAll('a'):
            #     #print(str(link.get('href')))
            #     dictionary[str(link.get('href'))] = dict()
            #     if depth > 1:
            #         adding(str(link.get('href')), dictionary[str(link.get('href'))], depth-1)


            resp = re.findall(r'(href|src|url)=\"([^\"]*)\"', root_URI.text)
            relative_to_absolute(URI, resp)
            for link in resp:
                dictionary[link] = dict()
                if depth > 1:
                    adding(link, dictionary[link], depth-1)

    except Exception as e:
        pass


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
