import os
import shutil
import math

# Paths
source_folder = r"youtube_copy"
destination_base = r"youtube_copy_split"

# Number of items per subfolder
items_per_folder = 15

# Create destination base folder if it doesn't exist
os.makedirs(destination_base, exist_ok=True)

# Get the list of files in the source folder
files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
total_files = len(files)

# Calculate the number of subfolders needed
num_subfolders = math.ceil(total_files / items_per_folder)

# Distribute files into subfolders
for i in range(num_subfolders):
    subfolder_path = os.path.join(destination_base, f"subfolder_{i+1}")
    os.makedirs(subfolder_path, exist_ok=True)
    start_index = i * items_per_folder
    end_index = start_index + items_per_folder
    for file in files[start_index:end_index]:
        shutil.move(os.path.join(source_folder, file), os.path.join(subfolder_path, file))

print(f"Files have been split into {num_subfolders} subfolders with up to {items_per_folder} items each.")
