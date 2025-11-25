# 4 write a python program to print the content of a diresctory using the os module.
import os

# Path of the directory you want to list
directory = "C:/Users/palak/Desktop/python-learning-journey"

# Check if the directory exists
if os.path.exists(directory):
    print(f"Contents of directory: {directory}\n")

    # List all files and folders
    for item in os.listdir(directory):
        print(item)
else:
    print("Directory does not exist.")