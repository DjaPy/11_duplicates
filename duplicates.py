import os
from argparse import ArgumentParser


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
            file_statistic = (entry.stat().st_size, entry.name, entry.path)
            files_list.append(file_statistic)
        elif entry.is_dir(follow_symlinks=False):
            files_list.extend(get_files_in_path(entry.path))
    return files_list


def take_first_index(elem):
    return elem[0]


def search_duplicates(file_list):
    duplicate_list = []
    start_index = 0
    const = 1
    half = 2
    end_index = len(files_list) - const
    medium_index = end_index // half

    for file in file_list:
        while medium_index != file[0] and start_index < end_index:
            if file[0] > files_list[medium_index][0]:
                start_index = medium_index + const
            else:
                end_index = medium_index - const
            medium_index = (start_index + end_index // half)
        search_index = medium_index

        if file_list[start_index][1] == file[1]:
            duplicate_list.append(file)
            file_list.pop(search_index)
    return duplicate_list


def display_the_result():
    for info_about_file in duplicate_list:
        duplicae_file = 'File {} duplicated on the way {}'.format(info_about_file[1], info_about_file[2])
        print(duplicate_file)


if __name__ == '__main__':
    option = get_path()
    path = option.path
    files_list = get_files_in_path(path)
    files_list.sort(key=take_first_index)
    print(files_list)
    duplicate_list = search_duplicates(files_list)
    display_the_result()
