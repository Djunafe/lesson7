"""Задание 2"""
"""Создайте два класса Directory(папка) и File(файл) с типами (анотацией)"""

from __future__ import annotations
from typing import *


data = TypeVar("type_directory")


class Directory:

    def __init__(self, name: str, root: data, files: list, sub_directories: list) -> None:
        self.name = name
        self.root = root
        self.files = files
        self.sub_directories = sub_directories

    def add_sub_directory(self, direct: data):
        direct.root = self.name
        return self.sub_directories.append(self)

    def remove_sub_directory(self) -> None:
        self.root = None
        return self.sub_directories.remove(self)

    def add_file(self, file: 'File'):
        file.direct = self.name
        return self.files.append(file)

    def remove_file(self, file: 'File'):
        file.direct = None
        return self.files.append(file)


class File:
    def __init__(self, name: str, directory: 'Directory' = None):
        self.name = name
        self.directory = directory


main_dir = Directory('main_dir', 'main', [], [])
direct1 = Directory('dir1', None, [], [])
direct2 = Directory('dir2', None, [], [])
file_1 = File('text_1.txt')
file_2 = File('text_2.txt')

main_dir.add_sub_directory(direct1)
main_dir.add_sub_directory(direct2)

main_dir.add_file(file_1)
direct1.add_file(file_2)

print(f'file : {file_1.name} is in directory : {file_1.directory} \nfile : {file_2.name} is in directory : '
      f'{file_2.directory} -->  Which is in directory : {direct1.root}')
