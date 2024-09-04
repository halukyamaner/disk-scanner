"""
Library: Disk Scanner
Author: Haluk YAMANER
Email: haluk@halukyamaner.com
Web: https://www.halukyamaner.com
Version: 1.0

Description:
    Disk Scanner is designed to meticulously traverse through a specified root directory, cataloging each sub-directory and file it encounters. This process results in the generation of two output files: 'Folders.txt' and 'Files.txt', which respectively list the paths of directories and files discovered. The script also displays these paths in real-time on the console for monitoring purposes.

Usage:
    To execute the script, run it from the command line. It is initially set to scan the root directory '/', suitable for Unix-based systems, but this can be adjusted in the script's source code to explore different directories. Upon completion, the script produces 'Folders.txt' and 'Files.txt' in the directory where the script was run.

Requirements:
    Python 3.x
    Modules: os

Features:
    - Conducts an exhaustive scan starting from the root directory or a specified starting point.
    - Compiles and outputs directory and file paths into two distinct text files.
    - Offers real-time console output of the scanning process for immediate feedback.

Warnings:
    - By default, the script scans from the root directory '/', which demands appropriate permissions and may consume considerable time on extensive file systems. Adjust the 'root_directory' variable to tailor the scan to specific needs.
    - Ensure the script is executed with the necessary permissions, especially when accessing system directories.
"""
import os

def scan_system(root_dir):
    # Initialize lists to store folders and files
    folders = []
    files = []

    # Walk through the directory structure
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            folder_path = os.path.join(dirpath, dirname)
            folders.append(folder_path)
            # Print the folder being scanned
            print(f"Scanning Folder: {folder_path}")

        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            files.append(file_path)
            # Print the file being scanned
            print(f"Scanning File: {file_path}")

    # Write folders to a text file
    with open('Folders.txt', 'w') as folder_file:
        for folder in folders:
            folder_file.write(f"{folder}\n")

    # Write files to a text file
    with open('Files.txt', 'w') as file_file:
        for file in files:
            file_file.write(f"{file}\n")

if __name__ == "__main__":
    # Define the root directory to scan
    root_directory = "/"  # Use "/" for scanning the entire system on Unix-based systems

    # Call the function to start scanning
    scan_system(root_directory)

    print("Scanning Completed! Check 'Folders.txt' and 'Files.txt' for results.")
