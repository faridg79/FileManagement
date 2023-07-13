# File Management Script

This script organizes files in a source directory based on their file extension and the modified year. It categorizes files into different folders such as photos, videos, text, and audio.

## Prerequisites

- Python 3.x

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/faridg79/FileManagement.git

1. Run the script by providing the source directory and destination directory as command-line arguments:
   ```bash
   python filemanagement.py source_directory destination_directory
   
Replace **source_directory** with the path to the directory containing the files you want to organize, and **destination_directory** with the path to the directory where you want to move the organized files.

2. The script will scan the source directory, categorize the files, and move them to the appropriate folders inside the destination directory.

# Example
Suppose you have the following file structure:

   ```bash
    - source_directory
     - image.jpg
     - video.mp4
     - audio.wav
     - document.docx

Running the script with the following command:

   ```bash
     python filemanagement.py source_directory destination_directory

will result in the following structure:

    ```bash
     - destination_directory
      - 2022
          - photos
              - image.jpg
          - videos
              - video.mp4
          - audio
              - audio.wav
          - text
              - document.docx

The files are organized based on their file extensions and the modified year.

# Supported File Extensions
+ Photos: jpg, jpeg, png
+ Videos: mp4, avi, 3gp, mpeg, mkv, wmv, mov
+ Audio: mp3, wav, flac
+ Text: txt, doc, docx


