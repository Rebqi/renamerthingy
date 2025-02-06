import os

# Define source and target directories
source_directory = "Source Directory here (the files that have the mp_m_freemode thing)"
target_directory = "Output Directory for the normal files"

# Ensure the target directory exists
os.makedirs(target_directory, exist_ok=True)

# Define the valid prefixes based on the provided categories
categories = {
    "head": "head_",
    "berd": "berd_",
    "hair": "hair_",
    "uppr": "uppr_",
    "lowr": "lowr_",
    "hand": "hand_",
    "feet": "feet_",
    "teef": "teef_",
    "accs": "accs_",
    "task": "task_",
    "decl": "decl_",
    "jbib": "jbib_",
    "p_eyes": "p_eyes_",
    "p_head": "p_head_",
}

# Get a list of all files in the source directory
files = [f for f in os.listdir(source_directory) if os.path.isfile(os.path.join(source_directory, f))]

# Sort the files alphabetically
files.sort()

# Iterate through each category
for category, prefix in categories.items():
    # Filter files matching the current category
    matching_files = [f for f in files if f.startswith(prefix)]
    
    # Initialize a counter for renaming
    counter = 1
    
    # Rename and move each file in the category
    for filename in matching_files:
        # Split the filename into name and extension
        _, extension = os.path.splitext(filename)
        
        # Generate the new name with the category prefix and counter
        new_name = f"{prefix}{counter:03}{extension}"
        
        # Define the source and target file paths
        old_file_path = os.path.join(source_directory, filename)
        new_file_path = os.path.join(target_directory, new_name)
        
        # Move and rename the file
        os.rename(old_file_path, new_file_path)
        
        print(f"Renamed and moved: {filename} -> {new_name}")
        
        # Increment the counter
        counter += 1

print("Renaming and sorting complete.")
