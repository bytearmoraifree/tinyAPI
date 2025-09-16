# ----- Info ------------------------------------------------------------------

__author__ = 'Michael Montero <mcmontero@gmail.com>'

# ----- Imports ---------------------------------------------------------------

import subprocess

__all__ = [
    'find_dirs',
    'find_files'
]

# ----- Public Functions ------------------------------------------------------

def find_dirs(path, pattern=None):
    '''Finds directories starting at the specified path and matching the
       specified pattern.'''
    if not os.path.isdir(path):
        return []

    matched_dirs = []
    for root, dirs, files in os.walk(path):
        for d in dirs:
            if pattern is None or fnmatch.fnmatch(d, pattern):
                matched_dirs.append(os.path.join(root, d))
    return matched_dirs


def find_files(path, pattern=None):
    '''Finds files starting at the specified path and matching the specified
       pattern.'''
    if not os.path.isdir(path):
        return []

    matched_files = []
    for root, dirs, files in os.walk(path):
        for f in files:
            if pattern is None or fnmatch.fnmatch(f, pattern):
                matched_files.append(os.path.join(root, f))
    return matched_files
