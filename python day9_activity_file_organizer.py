import os
import shutil

folder_path = "C:\Users\emer\Desktop\test_folder"

file_types = {

    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".csv"],
    "Archives": [".zip", ".rar"],
    "Scripts": [".py", ".js", ".html"]
}

def organize_files(path):
    for file in os.listdir(path):
        full_path = os.path.splitext(file)

        if os.path.isfile(full_path):
            _, ext = os.path.splitext(file)
            ext - ext.lower()

            moved = False
            for folder, extensions in file_types.items():
                if ext in extensions:
                    target_folder = os.path.join(path, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(full_path, os.path.join(target_folder, file))
                    print(f"Moved {file} ➜ {folder}")
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(path, Others)
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(full_path, os.path.join(other_folder, file))
                print(f"Moved {file} ➜ Others " )