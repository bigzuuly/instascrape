"""Get follower count for each user"""

# Standard library Imports
import argparse
import json
import logging
import time

from string import Template

# Third Party Library Imports
import requests

from bs4 import BeautifulSoup

# Local Application Imports


logger = logging.getLogger(__name__)

INSTAGRAM_FOLLOWERS_TEMPLATE = Template("https://www.instagram.com/$username/#")
DATA_PATH = "./merged_data/followers.json"
FOLLOWER_DATA_PATH = "./follower_data"

def main():

    print("Starting Instascrape to get follower count")

    with open(DATA_PATH, "r") as data_file:
      data = json.load(data_file)
      print("Number of Users:", len(data["users"]))

      for user in data["users"]:
        username = user["username"]
        print(f"Getting follower count for: {username}")
        url = INSTAGRAM_FOLLOWERS_TEMPLATE.substitute(username=username)

        response = requests.get(url=url)
        if response.status_code == 200:
            html_content = response.text

            # Process the HTML content
            soup = BeautifulSoup(html_content, features="html.parser")
            for meta in soup.find_all("meta"):
              property = meta.get("property")
              if property and property=="og:description":
                content_list = meta.get("content").split()

                follower_count = content_list[0].replace("K", "000").replace("M", "000000")
                print(f"Total Followers:{follower_count} - {meta}")
                user_content = {
                   "followers": follower_count,
                   "html_content": str(meta)
                }

                with open(FOLLOWER_DATA_PATH +"/" + user["id"] + ".json", "w") as file:
                  json.dump(user_content, file)
        else:
            print(f"Request failed with status code {response.status_code}")

      

        print("SLEEPING 1 SECONDS")
        time.sleep(1)


if __name__ == '__main__':
    main()
