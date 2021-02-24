import hashlib
import os

from tqdm import tqdm


def generate_file_hash(checksum_type: str, file_path: str):

    if checksum_type in hashlib.algorithms_available:

        with open(file_path, "rb") as f:
            checksum = hashlib.new(checksum_type)
            total_size = os.path.getsize(file_path)

            with tqdm(total=total_size, unit='B', unit_scale=True) as pbar:

                while True:
                    chunk = f.read(8192)
                    if not chunk:
                        break

                    checksum.update(chunk)
                    pbar.update(len(chunk))

        return checksum.hexdigest()

    raise TypeError(f"Checksum type: {checksum_type} not supported")
