import os
from argparse import ArgumentParser
from operator import itemgetter
from collections import defaultdict


def get_path():
    parser = ArgumentParser()
    parser.add_argument('path', help='The path to the directory'
                        ' for finding duplicate files', type=str)
    options = parser.parse_args()
    return options


def get_files_in_path(path):
    files_list = []
    for entry in os.scandir(path):
        if entry.is_file(follow_symlinks=False):
            file_statistic = ((entry.stat().st_size, entry.name), entry.path)
            files_list.append(file_statistic)
        elif entry.is_dir(follow_symlinks=False):
            files_list.extend(get_files_in_path(entry.path))
    return files_list


def search_duplicates(file_list):
    counter_keys = defaultdict(list)
    for file_info, path_file in file_list:
        counter_keys[file_info].append(path_file)
    duplicate_list = sorted(counter_keys.items())
    return duplicate_list


def display_the_result(duplicate_list):
    for info_about_file in duplicate_list:
        duplicate_file = 'File {} duplicated on the way:'.format(info_about_file[0][1])
        print(duplicate_file)
        for number, pathes_to_duplicate_files in enumerate(info_about_file[1]):
            info_about_path = '{}. {}'.format(number, pathes_to_duplicate_files)
            print(info_about_path)


if __name__ == '__main__':
    option = get_path()
    path = option.path
    file_list = get_files_in_path(path)
    print(search_duplicates(file_list))
    duplicate_list = search_duplicates(file_list)
    print(display_the_result(duplicate_list))
