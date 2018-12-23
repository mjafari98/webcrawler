from bs4 import BeautifulSoup as bs
import json
import requests
import re

ignoring_hosts = ['youtube',
                  'telegram',
                  'facebook',
                  'twitter',]

ignoring_formats = ['.css',
                    '.js',
                    '.jpg',
                    '.png',
                    '.svg',
                    '.ico',]

domain_list = ['.ir',
               '.com',
               '.org',
               '.net',]

def relative_to_absolute(BASE_URI, links):
    deleting_list = list()
    for i in range(0, len(links)):
        if links[i] == None:
            deleting_list.append(links[i])
            pass

        elif len(links[i]) < 1:
            deleting_list.append(links[i])
            pass

        elif links[i][:4] == 'http':
            pass

        elif any(domain in links[i] for domain in domain_list):
            pass

        elif links[i][0] == '/':
            a = links[i]
            if BASE_URI[-1] != '/':
                links[i] = BASE_URI + a
            elif BASE_URI[-1] == '/':
                links[i] = BASE_URI[:-1] + a

        else:
            a = links[i]
            if BASE_URI[-1] != '/':
                links[i] = BASE_URI + '/' + a
            elif BASE_URI[-1] == '/':
                links[i] = BASE_URI + a

    for x in deleting_list:
        links.remove(x)



def adding(URI, dictionary, depth):
    # try:
    if depth > 0:
        if any(host in URI for host in ignoring_hosts) or \
           any(format in URI for format in ignoring_formats):
            pass

        else:
            # Send GET request to take the HTML DOC from the URI
            root_URI = requests.get(URI)

            if root_URI.status_code == 200:
                # Render HTML_DOC from string to beautifulsoup
                # soup = bs(root_URI.text, 'html.parser')

                resp = list()
                resp.extend(re.findall(r'href=\"([^\"]*)\"', root_URI.text))
                # resp.extend(re.findall(r'url=\"([^\"]*)\"', root_URI.text))
                # resp.extend(re.findall(r'src=\"([^\"]*)\"', root_URI.text))
                relative_to_absolute(URI, resp)

                for link in resp:
                    dictionary[link] = dict()
                    # print(dictionary)
                    if depth > 1:
                        adding(link, dictionary[link], depth-1)

    # except Exception as e:
    #     print()


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
