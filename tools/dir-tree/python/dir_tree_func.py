import os
import sys

# TODO: fix the printing on algo course


def file_walk(path, depth=0, _prefix=""):
    max_depth = depth
    folders = 0
    files = 0
    current_dir = sort_dir_list(path)

    for index in range(len(current_dir)):

        new_path = os.path.join(path, current_dir[index])
        is_dir = os.path.isdir(new_path)
        if index == len(current_dir)-1:
            print_lines(_prefix, "└──", current_dir[index], is_dir)
            if is_dir:
                folders += 1
                new_folders, new_files, new_depth = file_walk(
                    new_path, depth+1, _prefix+"   ")
                if new_depth > max_depth:
                    max_depth = new_depth
                folders += new_folders
                files += new_files
            else:
                files += 1

        else:
            print_lines(_prefix, "├──", current_dir[index], is_dir)
            if is_dir:
                folders += 1
                new_folders, new_files, new_depth = file_walk(
                    new_path, depth+1, _prefix+" │  ")

                if new_depth > max_depth:
                    max_depth = new_depth
                folders += new_folders
                files += new_files
            else:
                files += 1

    return folders, files, max_depth


def sort_dir_list(path):
    dir_list = os.listdir(path)
    dir_list = filter(lambda x: x[0] != ".", dir_list)

    return sorted(dir_list, key=lambda x: not os.path.isdir(x))


def print_lines(_prefix, symbol, dir_name, is_dir=False):
    if is_dir:
        print(_prefix, symbol, "\033[94m"+dir_name+"\033[0m")
    else:
        print(_prefix, symbol, "\033[0m"+dir_name+"\033[0m")


if __name__ == "__main__":
    path = "."
    if len(sys.argv) > 1:
        path = sys.argv[1]

    if os.path.exists(path):
        print("\033[94m "+path+"\033[0m")
        folders, files, max_depth = file_walk(path)
    else:
        print(f"error can't find path: {path}")
        folders, files, max_depth = 0, 0, 0
    print(f"Folders: {folders}, Files: {files}, Max Depth: {max_depth}")
