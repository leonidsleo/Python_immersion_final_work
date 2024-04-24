import os
from collections import namedtuple


directory_description = namedtuple('directory_description', ['root_directory', 'name', 'extension', 'this_is_directory'])

def checking_object(directory):
    """
    функция обхода дирректории и нахождения объектов
    """
    
    file_directory = []
    for i in os.scandir(directory):
        name = os.path.splitext(i.name)[0] if i.is_file() else i.name
        extension = os.path.splitext(i.name)[1] if i.is_file() else None
        this_is_directory = i.is_dir()
        root_directory = os.path.basename(directory)

        file_object = directory_description(root_directory, name, extension, this_is_directory)
        file_directory.append(file_object)
    return file_directory