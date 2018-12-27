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

ignoring_notation = [':', '{', '#', '@']


def relative_to_absolute(BASE_URI, links):

    # find the base domain
    BASE_URI = regex.search(r'''(https?://[^/]*/*)''', BASE_URI).group(0)

    deleting_list = list()
    for i in range(0, len(links)):

        # append to delete list if the link is None(null)
        if links[i] == None:
            deleting_list.append(links[i])

        # append to delete list if length of the link is 0
        elif len(links[i]) < 1:
            deleting_list.append(links[i])

        elif any(notation in links[i] for notation in ignoring_notation):
            deleting_list.append(links[i])

        # if it's a url without hostname add the hostname to it
        elif not any(domain in links[i] for domain in domain_list) \
        and links[i][:4] != 'http':
            a = links[i]
            if BASE_URI[-1] != '/':
                links[i] = BASE_URI + '/' + a
            elif BASE_URI[-1] == '/':
                links[i] = BASE_URI + a

        # if a URI doesn't start with http it will be removed
        if links[i][:4] != 'http':
            deleting_list.append(links[i])

    return [e for e in links if e not in deleting_list]


def adding(URI, dictionary, depth):
    if depth > 0:
        if any(host in URI for host in ignoring_hosts) or \
           any(format in URI for format in ignoring_formats):
            pass

        else:
            # Send GET request to take the HTML DOC from the URI
            try:
                root_URI = requests.get(URI)
                root_URI.encoding = 'utf-8'

                if root_URI.status_code == 200:
                    resp = list()

                    # Regex to get href attributes
                    regexp_href_link = r'''href=\"(http[s]?://[^\"]*)\"'''
                    regexp_href_url  = r'''href=\"/*([^\"]*)\"'''
                    resp.extend(regex.findall(regexp_href_link, root_URI.text))
                    resp.extend(regex.findall(regexp_href_url, root_URI.text))

                    # Regex to get src attributes
                    # regexp_src_link = r'''src=\"(https?://[^\"]*)\"'''
                    # regexp_src_url  = r'''src=\"/*([^\"]*)\"'''
                    # resp.extend(regex.findall(regexp_src_link, root_URI.text))
                    # resp.extend(regex.findall(regexp_src_url, root_URI.text))

                    # Regex to get url attributes
                    # regexp_url_link = r'''url=\"(https?://[^\"]*)\"'''
                    # regexp_url_url  = r'''url=\"/*([^\"]*)\"'''
                    # resp.extend(regex.findall(regexp_url_link, root_URI.text))
                    # resp.extend(regex.findall(regexp_url_url, root_URI.text))

                    resp = relative_to_absolute(URI, resp)

                    for link in resp:
                        dictionary[link] = dict()
                        # print(dictionary)
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

j = json.dumps(tree_of_hyperlinks, indent=4, ensure_ascii=False)
print(j)
