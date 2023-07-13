import datetime
import os
import sys
import time

arguments = sys.argv
source_directory = arguments[1]
destination_directory = arguments[2]

if not os.path.isdir(str(destination_directory)):
    os.mkdir(destination_directory)

all_walk = os.walk(str(source_directory))


def check_and_copyfile(folder_name, file_name) -> None:
    if not os.path.isdir(folder_name):
        os.makedirs(folder_name)
    with open(file_path, "rb") as file:
        read_binary_file = file.read()
    with open(f"{folder_name}/{file_name}", "wb") as file:
        write_binary_file = file.write(read_binary_file)


for dir_and_files in all_walk:
    for file_name in dir_and_files[2]:
        file_path = dir_and_files[0] + "/" + file_name
        file_extension = os.path.splitext(file_path)[1].replace(".", "").lower()
        modified_year = time.ctime(os.path.getmtime(file_path)).split()[-1]

        video_extensions = ("mp4", "avi", "3gp", "mpeg", "mkv", "wmv", "mov")
        image_extensions = ("jpg", "jpeg", "png")
        text_extensions = ("txt", "doc", "docx")
        audio_extensions = ("mp3", "wav", "flac")

        if file_extension in image_extensions + video_extensions + text_extensions + audio_extensions:
            if not os.path.isdir(destination_directory + "/" + str(modified_year)):
                os.makedirs(destination_directory + "/" + str(modified_year))

            if file_extension in image_extensions:
                image_folder = destination_directory + "/" + str(modified_year) + "/photos"
                check_and_copyfile(image_folder, file_name)

            elif file_extension in video_extensions:
                video_folder = destination_directory + "/" + str(modified_year) + "/videos"
                check_and_copyfile(video_folder, file_name)


            elif file_extension in text_extensions:
                text_folder = destination_directory + "/" + str(modified_year) + "/text"
                check_and_copyfile(text_folder, file_name)

            elif file_extension in audio_extensions:
                audio_folder = destination_directory + "/" + str(modified_year) + "/audio"
                check_and_copyfile(audio_folder, file_name)
