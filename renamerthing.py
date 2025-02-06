import os
import shutil

# Hardcoded directories
source_directory = "folder of the stuff"
target_directory = "folder for the stuff to be put into"

# Verify that the source directory exists
if not os.path.exists(source_directory):
    print(f"Directory '{source_directory}' doesnt exist.")
    exit(1)
# Loop through each file in the source directory
for filename in os.listdir(source_directory):
    if "^" in filename:
        # Split the filename at the caret and keep only the part after it
        new_name = filename.split("^", 1)[1]

        # Full paths for the old and new files
        old_file = os.path.join(source_directory, filename)
        new_file = os.path.join(target_directory, new_name)

        # Rename and move the file to the target directory
        shutil.move(old_file, new_file)
        print(f"Renamed and Moved Files: {filename} -> {new_name}")

print("Renaming and moving done.")
