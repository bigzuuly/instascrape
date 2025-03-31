"""Merge individual follower dataset into a single JSON file"""

# Standard library Imports
import argparse
import json
import logging
import os

# Third Party Library Imports

# Local Application Imports


logger = logging.getLogger(__name__)

DATA_FOLDER = "./data"
MERGED_DATA_FOLDER = "./merged_data"

def main():

    print(f"Starting Data Merge from {DATA_FOLDER} to  {MERGED_DATA_FOLDER}")

    merged_data = {
        "users": []
    }

    with os.scandir(DATA_FOLDER) as it:
      for entry in it:
          if entry.name.endswith(".json") and entry.is_file():
              #print(entry.name, entry.path)
              with open(entry.path, "r") as data_file:
                  data = json.load(data_file)
                  for user in data["users"]:
                      merged_data["users"].append(user)


    print("Total Followers:", len(merged_data["users"]))

    with open(MERGED_DATA_FOLDER + "/followers.json", "w") as file:
        json.dump(merged_data, file, indent=2)

if __name__ == '__main__':
    main()
