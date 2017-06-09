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
    list_size_and_name = []
    for file_info in files_list:
        list_size_and_name.append((file_info[0], file_info[1]))
    return list_size_and_name
    

def search_duplicates(list_size_and_name):
    duplicate_list = []
    for index,file_check in enumerate(list_size_and_name):
        for file in list_size_and_name[(index+1):]:
            if file_check == file:
                duplicate_list.append(file_check)
    return(duplicate_list)


def get_full_info(duplicate_list, files_list):
    full_info_duplicate = []
    for file in files_list:
        for duplicate in duplicate_list:
            if file[0] == duplicate[0] and file[1] == duplicate[1]:
                full_info_duplicate.append(file)
    return full_info_duplicate

if __name__ == '__main__':
    path = '/path/to/folder'
    files_list = get_files_in_path(path)
    list_size_and_name = get_size_and_name(files_list)
    duplicate_list = search_duplicates(list_size_and_name)
    full_info_duplicate = get_full_info(duplicate_list, files_list)
    for full_info in full_info_duplicate:
        print(full_info)