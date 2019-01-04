import os
import os.path
import urllib.request


def rec(directory, current_path=''):
    for direc in directory:
        if type(directory[direc]) == dict:
            if direc[0] == '\\':
                direc = direc[1:]
            this_path = os.path.join(current_path, direc)
            this_path = this_path.replace('/', '\\')
            split_index = this_path.rfind('>')+1
            this_path = this_path[:split_index]
            if this_path[0] == "\\":
                rec(directory[direc], this_path[1:])
            else:
                rec(directory[direc], this_path)

        elif type(directory[direc]) == str:
            current_path += direc.replace('/', '\\')
            current_path = current_path[:current_path.rfind('>')]
            current_path = current_path.replace('>', '/')
            current_path = current_path.replace('/\\', '/')
            # print(directory[direc])
            try:
                os.makedirs(current_path)
            except Exception as e:
                pass

            filename = current_path + '/' + directory[direc].replace('/', '\\')
            try:
                urllib.request.urlretrieve(directory[direc], filename)
            except Exception as e:
                with open(filename, 'w+') as f:
                    f.write('This Website has restricted to download data')

                print('This Website has restricted to download data')
