import os

def walklevel(some_dir, level=1):
    # Remove trailing path separator
    some_dir = some_dir.rstrip(os.path.sep)

    # Make sure the directory exists
    assert os.path.isdir(some_dir)

    # Count the number of path separators in the directory path
    num_sep = some_dir.count(os.path.sep)

    # Traverse the directory tree using os.walk()
    for root, dirs, files in os.walk(some_dir):

        # Yield the current directory path, its subdirectories, and its files
        yield root, dirs, files

        # Count the number of path separators in the current directory path
        num_sep_this = root.count(os.path.sep)

        # If the current directory level exceeds the specified depth level, remove its subdirectories
        if num_sep + level <= num_sep_this:
            del dirs[:]
