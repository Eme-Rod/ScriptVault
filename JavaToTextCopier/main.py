import os


def get_folder_names(directory):
    """
    Get a list of folder names inside a directory.
    """
    folder_names = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if (os.path.isdir(item_path)) and (item != '.idea'):
            folder_names.append(item)
    return folder_names


def get_java_files(directory):
    """
    Get a list of java file names inside a directory.
    """
    files_names = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        item_name = os.path.splitext(item)[0]
        if (os.path.isfile(item_path)) and (item_name != 'testClass'):
            files_names.append(item_name)
    return files_names


def copy_java_to_txt(java_path, txt_path, name):
    """
    Copy the content of a Java file to a corresponding text file.
    """
    folder_path = os.path.join(txt_path, name)
    txt_name = name + '.java'
    os.mkdir(folder_path)
    file_path = os.path.join(folder_path, txt_name)

    with open(java_path, 'r') as file:
        java_content = file.read()

    with open(file_path, 'w') as destination_folder:
        destination_folder.write(java_content)


java_files_path = 'C:/Repos/Java/Java_practice/Intellij_hackerrank_exercises/src'
txt_folder_path = 'C:/Repos/Java/Java_practice/hackerrank_exercises'

txt_folders = get_folder_names(txt_folder_path)
java_files = get_java_files(java_files_path)

for file_name in java_files:
    if file_name not in txt_folders:
        java_file = os.path.join(java_files_path, file_name + '.java')
        copy_java_to_txt(java_file, txt_folder_path, file_name)
