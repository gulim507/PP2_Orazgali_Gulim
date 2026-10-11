import os
import shutil

# Create directories
os.makedirs("source_folder", exist_ok=True)
os.makedirs("destination_folder", exist_ok=True)

# Create a file
with open("source_folder/example.txt", "w") as file:
    file.write("Example file.")

# Copy file
shutil.copy(
    "source_folder/example.txt",
    "destination_folder/example_copy.txt"
)

print("File copied successfully.")

# Move file
shutil.move(
    "source_folder/example.txt",
    "destination_folder/example.txt"
)

print("File moved successfully.")

# Remove empty directory
if os.path.exists("source_folder"):
    os.rmdir("source_folder")

print("Directory management completed.")