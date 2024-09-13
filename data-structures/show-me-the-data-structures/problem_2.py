import os

def find_files(suffix: str, path: str) -> list[str]:
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Parameters:
    -----------
    suffix : str
        The suffix of the files to be found.
    path : str
        The root directory path where the search should begin.

    Returns:
    --------
    list[str]
        A list of file paths that end with the given suffix.
    """
    # real_path = os.getcwd()
    # real_path = os.path.dirname(os.path.realpath(__file__))

    # path = os.path.join(real_path,path[2:])
    main_dir_queue = os.listdir(path)
    main_dir_queue = [path + '/' + i for i in main_dir_queue]
    result = []
    
    while len(main_dir_queue) > 0:
        file = main_dir_queue.pop(0)
        if os.path.isdir(file):
            files = os.listdir(os.path.join(file))
            files = [file + '/' + i for i in files]
            # print(files)
            main_dir_queue += files
        elif os.path.isfile(file) :
            if file.endswith(suffix):
                result.append(file)
    return result


if __name__ == "__main__":
    # Test Case 1: Standard test case with known structure
    print("Test Case 1: Standard directory structure")
    result = find_files(".c", "./testdir")
    print(result)
    # Expected output: ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']

    # Test Case 2
    pass

    # Test Case 3
    pass