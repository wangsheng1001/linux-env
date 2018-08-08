import os.path
import logging
import ycm_core

BASE_FLAGS = [
        '-Wall',
        '-Wextra',
        '-Wno-long-long',
        '-Wno-variadic-macros',
        '-fexceptions',
        '-ferror-limit=10000',
        '-DNDEBUG',
        '-std=c++11',
        '-xc++',
        '-I/usr/lib/',
        '-I/usr/include/',
        ]

HEADER_DIRECTORIES = [
        'include'
        ]

def FindNearest(path, target):
    # check if target dir exists in the path
    candidate = os.path.join(path, target)
    if (os.path.isfile(candidate) or os.path.isdir(candidate)):
        logging.info("Found nearest " + target + " at " + candidate)
        return candidate
    # check if the path has parent dir
    parent = os.path.dirname(os.path.abspath(path))
    if (parent == path):
        return None
    return FindNearest(parent, target)

def FlagsForInclude(root):
    # find all possible locations containing project header files
    flags = []
    for header_dir in HEADER_DIRECTORIES:
        include_path = FindNearest(root, header_dir)
        if include_path:
            flags += ["-I" + include_path]
    return flags

def FlagsForFile(filename):
    root = os.path.realpath(filename)
    flags = BASE_FLAGS + FlagsForInclude(root)
    return {
            'flags': flags,
            'do_cache': True
            }
