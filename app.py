import argparse
import os
from pathlib import Path
import shutil

parser = argparse.ArgumentParser(description='Find files in the src, and add them to the dst but inside a folder')
parser.add_argument('--src', help="The location to search for files", required=True)
parser.add_argument('--dst', help="The location to create the directory and place the files", required=True)
args = parser.parse_args()
print(args.src, args.dst)

for root, dirs, files in os.walk(args.src):
    for name in files:
        destination_directory = Path(name).stem
        destination_file = name
        print("Will create '{}/{}/{}' from {}".format(args.dst, destination_directory, destination_file,
                                                      os.path.join(root, name)))
        print("Copying...")
        os.makedirs("{}/{}".format(args.dst, destination_directory), exist_ok=True)
        shutil.copy(os.path.join(root, name), "{}/{}/{}".format(args.dst, destination_directory, destination_file))
        print("Done copying...")
