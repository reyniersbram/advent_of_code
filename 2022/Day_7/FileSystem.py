from __future__ import annotations


class File:
    def __init__(self, parent: Directory, name: str, size: int):
        self.parent = parent
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def __str__(self):
        return f'{self.get_path()}: {self.size}'

    def get_path(self):
        if self.parent is None:
            return "/"
        return self.parent.get_path() + self.name

    @staticmethod
    def is_dir():
        return False


class Directory(File):
    def __init__(self, parent: Directory, name: str):
        super().__init__(parent, name, 0)
        self.root = parent.root if parent is not None else None
        self.files = {}

    def add_file(self, file: File):
        self.files[file.name] = file

    def get_size(self) -> int:
        size = 0
        for (_, file) in self.files.items():
            size += file.get_size()
        return size

    def cd(self, arg: str) -> Directory:
        if arg == "/":
            return self.root
        elif arg == "..":
            return self.parent
        return self.files[arg]

    def get_path(self):
        if self.parent is None:
            return "/"
        return self.parent.get_path() + self.name + "/"

    @staticmethod
    def is_dir():
        return True
