import hashlib
import os
import io
import json

def has_dupes(L):
    seen = set()
    result = []
    for x in L:
        if x in seen:
            result.append(x)
        seen.add(x)
    return result
    

def hash_directory(path, outfile):
    if os.path.exists(outfile):
        with open(outfile, "rb") as f:
            return json.load(f)

    result = []
    for root, directories, filenames in os.walk(path):
        for filename in filenames: 
            full_filename = os.path.join(root,filename)
            hasher = hashlib.sha512()
            with open(full_filename, "rb") as file_data:
                for block in iter(lambda: file_data.read(io.DEFAULT_BUFFER_SIZE), b''):
                    hasher.update(block)
            result.append((hasher.hexdigest(), full_filename))

    with open(outfile, "wb") as f:
        json.dump(result, f)

    return result

gphotos = hash_directory("./Google Photos", "GooglePhotos.json")
gphotos_hashes = [x[0] for x in gphotos]
gtakeout = hash_directory("./Google Takeout", "GoogleTakeout.json")
gtakeout_hashes = [x[0] for x in gtakeout]

#print has_dupes(gphotos_hashes)
#print has_dupes(gtakeout_hashes)

# for hash in gphotos_hashes:
#     if hash not in gtakeout_hashes:
#         print hash

# for hash in gtakeout_hashes:
#     if hash not in gphotos_hashes:
#         print hash

gphotos_hashes_sub = [x for x in gphotos_hashes if x not in gtakeout_hashes]
gtakeout_hashes_sub = [x for x in gtakeout_hashes if x not in gphotos_hashes]

# gphotos_sub = []
# for hash in gphotos_hashes_sub:
#     for x in gphotos:
#         if x[0] == hash:
#             gphotos_sub.append(x)
#             break

# for x in gphotos_sub:
#     print x[1]

gtakeout_sub = []
for hash in gtakeout_hashes_sub:
    for x in gtakeout:
        if x[0] == hash:
            gtakeout_sub.append(x)
            break

for x in gtakeout_sub:
    print x[1]