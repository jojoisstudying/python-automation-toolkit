import os
import argparse
from datetime import datetime

def rename_with_number(folder):
    files = sorted(os.listdir(folder))
    for index, filename in enumerate(files, start=1):
        new_name = f"{index:03d}_{filename}"
        src = os.path.join(folder, filename)
        dst = os.path.join(folder, new_name)
        os.rename(src, dst)
        print(f"Renamed: {filename} → {new_name}")

def rename_with_date(folder):
    files = sorted(os.listdir(folder))
    date = datetime.today().strftime('%Y-%m-%d')
    for filename in files:
        new_name = f"{date}_{filename}"
        src = os.path.join(folder, filename)
        dst = os.path.join(folder, new_name)
        os.rename(src, dst)
        print(f"Renamed: {filename} → {new_name}")

def rename_by_oldest(folder):
    # get files with their modification time
    files = os.listdir(folder)
    files_with_time = []
    
    for filename in files:
        filepath = os.path.join(folder, filename)
        modified_time = os.path.getmtime(filepath)  # get file's modified date
        files_with_time.append((filename, modified_time))
    
    # sort by date, oldest first
    files_with_time.sort(key=lambda x: x[1])
    
    # rename with ordered number
    for index, (filename, _) in enumerate(files_with_time, start=1):
        new_name = f"{index:03d}_{filename}"
        src = os.path.join(folder, filename)
        dst = os.path.join(folder, new_name)
        os.rename(src, dst)
        print(f"Renamed: {filename} → {new_name}")

parser = argparse.ArgumentParser(description="Bulk File Renamer")
parser.add_argument("folder", help="Path to the folder")
parser.add_argument("--mode", choices=["number", "date", "oldest"], default="number")
args = parser.parse_args()

if args.mode == "number":
    rename_with_number(args.folder)
elif args.mode == "date":
    rename_with_date(args.folder)
elif args.mode == "oldest":
    rename_by_oldest(args.folder)