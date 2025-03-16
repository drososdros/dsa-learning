import os
import sys


class DirTree:
    def __init__(self) -> None:
        self.dirs = 0
        self. files = 0

    def count(self, is_dir):
        if is_dir:
            self.dirs += 1
        else:
            self.files += 1

    def print(self, prefix, symbol, file, is_dir):
        if is_dir:
            print(prefix, symbol, "\033[94m"+file+"\033[0m", sep="")
        else:
            print(prefix, symbol, file, sep="")

    def walk(self, path=".", prefix=""):
        files = sorted(os.listdir(path), key=lambda x: x.casefold())
        for index, file in enumerate(files):
            if file[0] == ".":
                continue
            file_path = os.path.join(path, file)
            is_dir = os.path.isdir(file_path)
            self.count(is_dir)
            if index == len(files) - 1:
                self.print(prefix, "└──> ", file, is_dir)
                if is_dir:
                    self.walk(file_path, prefix + "    ")

            else:
                self.print(prefix, "├──> ", file, is_dir)
                if is_dir:
                    self.walk(file_path, prefix + "│  ")

    def run(self, path):
        if os.path.exists(path):
            print("\033[94m.\033[0m")
            self.walk(path)
        else:
            print(f"error can't find path: {path}")
        print(f"Directories: {self.dirs}, files: {self.files}")


if __name__ == "__main__":
    path = "."
    args = sys.argv
    if len(args) > 1:
        path = args[1]
    p = DirTree()
    p.run(path)
