import os
import shutil
import argparse

# define which extensions go into which folder
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".ico"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv"],
    "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Programs": [".exe", ".msi", ".dmg", ".apk"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".ts"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Others": []
}

def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return "Others"  # anything not matched goes here

def organize_folder(folder):
    files = os.listdir(folder)
    moved = 0

    for filename in files:
        filepath = os.path.join(folder, filename)

        # skip if its a folder not a file
        if os.path.isdir(filepath):
            continue

        ext = os.path.splitext(filename)[1]
        category = get_category(ext)

        # create the subfolder if it doesnt exist
        destination_folder = os.path.join(folder, category)
        os.makedirs(destination_folder, exist_ok=True)

        # move the file
        destination = os.path.join(destination_folder, filename)
        shutil.move(filepath, destination)
        print(f"Moved: {filename} → {category}/")
        moved += 1

    print(f"\nDone! {moved} files organized.")

parser = argparse.ArgumentParser(description="Folder Organizer")
parser.add_argument("folder", help="Path to the folder you want to organize")
args = parser.parse_args()

organize_folder(args.folder)