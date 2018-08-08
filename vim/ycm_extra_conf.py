import os
import os.path
import fnmatch
import logging
import ycm_core
import re

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

SOURCE_EXTENSIONS = [
        '.cpp',
        '.cxx',
        '.cc',
        '.c',
        '.m',
        '.mm'
        ]

SOURCE_DIRECTORIES = [
        'src',
        'lib'
        ]

HEADER_EXTENSIONS = [
        '.h',
        '.hxx',
        '.hpp',
        '.hh'
        ]

HEADER_DIRECTORIES = [
        'include'
        ]

BUILD_DIRECTORY = 'build';

def FindNearest(path, target, build_folder=None):
    # check if target dir exists in the path
    candidate = os.path.join(path, target)
    if(os.path.isfile(candidate) or os.path.isdir(candidate)):
        logging.info("Found nearest " + target + " at " + candidate)
        return candidate;

    # check if the path has parent dir
    parent = os.path.dirname(os.path.abspath(path));
    if(parent == path):
        raise RuntimeError("Could not find " + target);

    if(build_folder):
        candidate = os.path.join(parent, build_folder, target)
        if(os.path.isfile(candidate) or os.path.isdir(candidate)):
            logging.info("Found nearest " + target + " in build folder at " + candidate)
            return candidate;

    return FindNearest(parent, target, build_folder)

def FlagsForInclude(root):
    # find all possible locations containing project header files
    try:
        flags = []
        for header_dir in HEADER_DIRECTORIES:
            include_path = FindNearest(root, header_dir)
            if include_path:
                flags = flags + ["-I" + include_path]
        return flags
    except:
        return None

def FlagsForFile(filename):
    root = os.path.realpath(filename);
    final_flags = BASE_FLAGS
    include_flags = FlagsForInclude(root)
    if include_flags:
        final_flags = final_flags + include_flags
    return {
            'flags': final_flags,
            'do_cache': True
            }
