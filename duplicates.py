import os


def get_files_in_path(path):
    files_list = []
    for entry in os.scandir(path):
        if entry.is_file(follow_symlinks=False):
            file_statistic = (entry.name, entry.stat().st_size, entry.path)
            files_list.append(file_statistic)
        elif entry.is_dir(follow_symlinks=False):
            files_list.extend(get_files_in_path(entry.path))
    return files_list


def get_size_and_name(files_list):
    dict_files = {}
    for file_info in files_list:
        dict_files[(file_info[0], file_info[1])] = (file_info[2])
    return dict_files


def search_duplicates(dict_files):
    pass


def get_full_info(duplicate_set, dict_files):
    list_duplicate = []
    print(duplicate_set)
    for file_info in dict_files:
        if file_info in duplicate_set:
            list_duplicate.append(file_info)
            print(list_duplicate)
    return list_duplicate


if __name__ == '__main__':
    path = '/home/kento/devman'
    files_list = get_files_in_path(path)
    dict_files = get_size_and_name(files_list)
    duplicate_set = search_duplicates(dict_files)
    print(get_full_info(duplicate_set, dict_files))