import argparse
import hashlib
import os
import io


def hash_directory(path):
    results = {}
    for root, _, filenames in os.walk(path):
        for filename in filenames:
            full_filename = os.path.join(root, filename)
            hasher = hashlib.sha512()
            with open(full_filename, "rb") as file_data:
                for block in iter(lambda: file_data.read(io.DEFAULT_BUFFER_SIZE), b''):
                    hasher.update(block)
            results.setdefault(hasher.hexdigest(), []).append(full_filename)
    return results


def dict_subtraction(a, b):
    return {k: v for k, v in a.items() if k not in b}


def print_differences(path, a):
    if not len(a):
        return
    print("Files only in {}:".format(path))
    for _, file_list in a.items():
        for file_name in file_list:
            print(file_name)
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("DIR_A")
    parser.add_argument("DIR_B")
    args = parser.parse_args()

    # get flattened hashes for each directory
    a = hash_directory(args.DIR_A)
    b = hash_directory(args.DIR_B)

    # subtract the hashes and print results
    print_differences(args.DIR_A, dict_subtraction(a, b))
    print_differences(args.DIR_B, dict_subtraction(b, a))
