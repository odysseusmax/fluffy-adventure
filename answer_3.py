import pathlib
import hashlib


def calc_hash(file):
    hash = hashlib.sha1()
    file_obj = open(file, 'rb')
    for chunk in file_obj.read(1024):
        hash.update(chunk)
    file_obj.close()
    return hash.digest()


def find_duplicates(path):
    hash_table = {}
    for file in path.iterdir():
        file_hash = calc_hash(file)
        if not hash_table.get(file_hash):
            hash_table[file_hash] = [file.name]
        else:
            hash_table[file_hash].append(file.name)
    return [hash_table[hash] for hash in hash_table]

if __name__ == '__main__':
    for d in find_duplicates(pathlib.Path('')): # assuming script is run in the unzipped directory
        print(d)
