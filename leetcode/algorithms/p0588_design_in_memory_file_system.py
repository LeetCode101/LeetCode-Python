from typing import List


class File:
    def __init__(self, name, is_file=False):
        self.name = name
        self.is_file = is_file
        self.content = ''
        self.files = {}

    def search(self, path):
        paths = path.split('/')
        file = self

        for i in range(1, len(paths)):
            file = file.files.get(paths[i], None)

            if not file:
                return None

        return file

    def ls(self):
        if self.is_file:
            return [self.name]
        else:
            return sorted(list(map(lambda f: f.name,
                                   list(self.files.values()))))


class FileSystem:
    def __init__(self):
        self.root = File('')

    def ls(self, path: str) -> List[str]:
        if path == '/':
            return self.root.ls()

        file = self.root.search(path)

        return file.ls() if file else []

    def mkdir(self, path: str) -> None:
        self._make(path, False)

    def addContentToFile(self, filePath: str, content: str) -> None:
        file = self._make(filePath, True)
        file.content += content

    def readContentFromFile(self, filePath: str) -> str:
        file = self.root.search(filePath)

        return file.content if file else ''

    def _make(self, path, is_file):
        paths = path.split('/')
        file = self.root

        for i in range(1, len(paths)):
            files = file.files
            name = paths[i]

            if name not in files:
                file.files[name] = File(name)

            file = files[name]

        file.is_file = is_file

        return file
