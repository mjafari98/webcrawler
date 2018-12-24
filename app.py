from bs4 import BeautifulSoup as bs
import json
import requests
import regex

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

ignoring_notation = ['\{',
                     '\}']

def relative_to_absolute(BASE_URI, links):
    deleting_list = list()
    for i in range(0, len(links)):

        for char_counter in range(5):
            if links[i][0] == "/":
                links[i] = links[i][1:]
            else:
                break;

        # append to delete list if the link is None(null)
        if links[i] == None:
            deleting_list.append(links[i])

        # append to delete list if length of the link is 0
        elif len(links[i]) < 1:
            deleting_list.append(links[i])

        elif '{' in links[i] or '\\x' in links[i]:
            deleting_list.append(links[i])

        # don't change anything if it has http at the first of the link
        elif links[i][:4] == 'http':
            pass

        # don't change anything if it is a valid domain
        elif any(domain in links[i] for domain in domain_list):
            pass
        
        # if it's a url without hostname add the hostname to it
        # elif links[i][0] == '/':
        #     a = links[i]
        #     if BASE_URI[-1] != '/':
        #         links[i] = BASE_URI + a
        #     elif BASE_URI[-1] == '/':
        #         links[i] = BASE_URI[:-1] + a


        # if it's a url without hostname add the hostname to it
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
           any(format in URI for format in ignoring_formats) or \
           any(notation in URI for notation in ignoring_notation):
            pass

        else:
            # Send GET request to take the HTML DOC from the URI
            root_URI = requests.get(URI)
            root_URI.encoding = 'utf-8'

            if root_URI.status_code == 200:
                # Render HTML_DOC from string to beautifulsoup
                # soup = bs(root_URI.text, 'html.parser')

                resp = list()
                regexpattern = r'href=\"([^\"]*)\"'
                resp.extend(regex.findall(regexpattern, root_URI.text))
                # resp.extend(re.findall(r'url=\"([^\"]*)\"', root_URI.text))
                # resp.extend(re.findall(r'src=\"([^\"]*)\"', root_URI.text))
                relative_to_absolute(URI, resp)

                for link in resp:
                    dictionary[link] = dict()
                    print(dictionary)
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
