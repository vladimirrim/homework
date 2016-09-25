import sys
import os
from hashlib import md5
from collections import defaultdict


def get_file_hash(filename):
    with open(filename, 'rb') as f:
        h = md5()
        while True:
            data = f.read(8192)
            if not data:
                break
            h.update(data)
        value = h.hexdigest()
    return value


def find_duplicates(path):
    hash_dict = defaultdict(list)
    for root, dirs, files in os.walk(path):
        for file in files:
            if file[0] != '.' and file[1] != '~':
                current_file = os.path.join(root, file)
                hash_dict[get_file_hash(current_file)].append(current_file)
    for duplicates in hash_dict.values():
        if len(duplicates) > 1:
            print(':'.join(duplicates))


find_duplicates(sys.argv[1])

