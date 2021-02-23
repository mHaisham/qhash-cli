import hashlib
import os


def generate_file_hash(checksum_type: str, file_path: str):
    read_size = 0
    total_size = os.path.getsize(file_path)

    if checksum_type in hashlib.algorithms_available:
        with open(file_path, "rb") as f:
            checksum = hashlib.new(checksum_type)
            while chunk := f.read(8192):
                read_size += len(chunk)
                checksum.update(chunk)
                percentage_done = 100 * read_size / total_size
                print(round(percentage_done, 1), "%", end="\r")
        return checksum.hexdigest()
    return "Checksum type not supported!"
