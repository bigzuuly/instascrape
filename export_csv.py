"""Get follower count for each user"""

# Standard library Imports
import argparse
import csv
import json
import logging
import os
import time

# Third Party Library Imports
from bs4 import BeautifulSoup

# Local Application Imports


logger = logging.getLogger(__name__)

FOLLOWER_DATA_PATH = "./follower_data"
DATA_PATH = "./merged_data/followers.json"

def main():

    print("Exporting Follower Count as CSV")

    user_id_handle_map = {}
    merged_data = []

    with open(DATA_PATH, "r") as data_file:
      data = json.load(data_file)
      print("Number of Users:", len(data["users"]))
    
    for user in data["users"]:
       user_id_handle_map[user["id"]] = user["username"]

    with os.scandir(FOLLOWER_DATA_PATH) as it:
      for entry in it:
          if entry.name.endswith(".json") and entry.is_file():
              #print(entry.name, entry.path)
              with open(entry.path, "r") as data_file:
                  data = json.load(data_file)
                  key = entry.name.replace(".json", "")
                  merged_data.append({"instagram_handle": user_id_handle_map[key], "followers": data["followers"]})

    print("Total Followers:", len(merged_data))

    with open(FOLLOWER_DATA_PATH + "/followers.csv", "w", newline="") as csvfile:
      fieldnames = ["instagram_handle", "followers"]
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      writer.writeheader()
      writer.writerows(merged_data)

if __name__ == '__main__':
    main()
