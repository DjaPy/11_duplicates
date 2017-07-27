import os
from argparse import ArgumentParser
from collections import defaultdict


def get_path():
    parser = ArgumentParser()
    parser.add_argument('path', help='The path to the directory'
                        ' for finding duplicate files', type=str)
    options = parser.parse_args()
    return options


def get_files_in_path(path):
    intermediate_list = defaultdict(list)
    for root, dirs, files in os.walk(path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_info = os.path.getsize(file_path)
            intermediate_list[file_info, file_name].append(file_path)
    return intermediate_list


def search_duplicates(intermediate_list):
    duplicate_list = defaultdict(list)
    for name_file, pathes in intermediate_list.items():
        if len(pathes) > 1:
            duplicate_list[name_file].extend(pathes)
    return duplicate_list


def display_the_result(duplicate_list: defaultdict):
    for name_file, pathes in duplicate_list.items():
        duplicate_file = 'Duplicate a file "{}" size of {} kb'.format(name_file[1], name_file[0])
        number_copies = '| {} сopies'.format(len(pathes))
        print(duplicate_file)
        print(number_copies)
        for path in pathes:
            path_to_file = '| Location: {}'.format(path)
            print(path_to_file)
        print()



if __name__ == '__main__':
    option = get_path()
    intermediate_files_list = get_files_in_path(option.path)
    duplicate_list = search_duplicates(intermediate_files_list)
    display_the_result(duplicate_list)