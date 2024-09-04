# Disk Scanner

## Overview
Disk Scanner is a Python script designed to traverse through a specified root directory, cataloging each sub-directory and file it encounters. This helps in generating comprehensive listings of all directories and files within the root directory or any specified starting point.

## Features
- **Exhaustive Scanning**: Starts scanning from the root directory or any specified starting point.
- **Output Files Generation**: Generates 'Folders.txt' and 'Files.txt' which list all the directories and files discovered during the scan.
- **Real-Time Console Output**: Displays paths of directories and files in real-time on the console for monitoring purposes.

## Requirements
- Python 3.x
- `os` module

## Usage
To use Disk Scanner, run the script from the command line. It is initially configured to scan the root directory '/', which is suitable for Unix-based systems. This can be modified in the script's source code to scan different directories.

```bash
python disk_scanner.py
