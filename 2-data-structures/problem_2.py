import os


def find_files(suffix, path):
    files = []

    def traverse(suffix, path):
        if os.path.isfile(path) and path.endswith(suffix):
            files.append(path)
        elif os.path.isdir(path):
            for file in os.listdir(path):
                traverse(suffix, os.path.join(path, file))

        return files

    traverse(suffix, path)
    return files


if __name__ == '__main__':
    print(find_files('.c', './testdir'))
    print(find_files('.h', './testdir'))
    print(find_files('.gitkeep', './testdir'))
