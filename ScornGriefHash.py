import os
import hashlib
from tqdm import tqdm

def get_md5(filename):
    """Calculate the MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def rename_files():
    """Rename all files in the directory to their MD5 hashes and change the extensions to .md5."""
    current_dir = os.path.dirname(os.path.realpath(__file__))
    all_files = [f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))]
    
    renamed_count = 0
    skipped_count = 0
    
    with tqdm(total=len(all_files), desc="Total Progress") as pbar_total:
        for filename in all_files:
            file_path = os.path.join(current_dir, filename)
            file_hash = get_md5(file_path)
            new_filename = file_hash + ".md5"
            try:
                os.rename(file_path, os.path.join(current_dir, new_filename))
                renamed_count += 1
                tqdm.write(f"Renamed {filename} to {new_filename}")
            except Exception as e:
                skipped_count += 1
                tqdm.write(f"Skipped renaming {filename}: {str(e)}")
            pbar_total.update(1)
    
    tqdm.write(f"All files have been hashed and renamed successfully. Renamed: {renamed_count}, Skipped: {skipped_count}")

if __name__ == "__main__":
    rename_files()
