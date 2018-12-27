import os
import os.path


def rec(directory, current_path=''):
    for direc in directory:
        if type(directory[direc]) == dict:
            this_path = os.path.join(current_path, direc)
            this_path = this_path.replace('/', '\\')
            split_index = this_path.rfind('>')+1
            this_path = this_path[:split_index]
            rec(directory[direc], this_path)

        elif type(directory[direc]) == str:
            current_path += direc.replace('/', '\\')
            current_path = current_path.replace('>', '/')
            current_path = current_path[:current_path.rfind('>')]
            os.makedirs(current_path)
