from bs4 import BeautifulSoup as bs
import json
import requests
import re

def pull_out(the_root_URI_input_i, depth_i):
    ignoring_hosts = ['youtube',
                      'telegram',
                      'facebook',
                      'twitter',
                      ]

    def adding(URI, dictionary, depth):
        try:
            if depth > 0:
                if any(host in URI for host in ignoring_hosts):
                    pass
                else:
                    # Send GET request to take the HTML DOC from the URI
                    root_URI = requests.get(URI)

                    # Render HTML_DOC from string to beautifulsoup
                    soup = bs(root_URI.text, 'html.parser')

                    # Query on beautifulsoup to pull out hyperlinks
                    for link in soup.find_all('a', attrs={'href': re.compile("^http[s]*://")}):
                        dictionary[str(link.get('href'))] = dict()
                        if depth > 1:
                            adding(str(link.get('href')), dictionary[str(link.get('href'))], depth-1)

        except Exception as e:
            print(e)


    # The tree of links appends here
    tree_of_hyperlinks = dict()

    # Root URI that we want to conduct analysis on it
    the_root_URI_input = the_root_URI_input_i

    # Get the depth of analysing
    depth = depth_i

    # initialize dictionary
    tree_of_hyperlinks[the_root_URI_input] = dict()

    # web scraping starts here!
    adding(the_root_URI_input, tree_of_hyperlinks[the_root_URI_input], depth)

    j = json.dumps(tree_of_hyperlinks, indent=4)
    j2 = json.loads(j)
    return j2
