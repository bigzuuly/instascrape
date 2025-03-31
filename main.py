"""Entrypoint for Instascrape"""

# Standard library Imports
import argparse
import json
import logging
import time

from string import Template

# Third Party Library Imports
import requests

# Local Application Imports


logger = logging.getLogger(__name__)

# UPDATE THE FOLLOWING WITH YOUR INSTGRAM SESSION
COOKIE = 'GRAB ENTIRE COOKIE'
X_IG_APP_ID = "IG APP ID"
X_ASBD_ID = "IG ASBD ID"
X_IG_WWW_CLAIM = "IG WWW CLAIM"

# UPDATE THE FOLLOWING WITH THE ACCOUNT TO SCRAPE
INSTAGRAM_URL = "https://www.instagram.com"
REFERER = "https://www.instagram.com/megacatproject/followers/"
ACCOUNT_NAME = "megacatproject"
INSTAGRAM_ACCOUNT_ID = "54057496414"

#### FOLLOWER API
INSTAGRAM_FOLLOWERS_TEMPLATE = Template("https://www.instagram.com/api/v1/friendships/$account_id/followers/?count=25&max_id=$next_max_id&search_surface=follow_list_page")


def main():

    print("Starting Instascrape")
    print(f"Account to Scrape: {ACCOUNT_NAME}")

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0",
        "Cookie": COOKIE,
        "Host": "www.instagram.com",
        "Referer": REFERER,
        "X-IG-App-ID": X_IG_APP_ID,
        "X-ASBD-ID": X_ASBD_ID,
        "X-IG-WWW-Claim": X_IG_WWW_CLAIM,
        "X-Requested-With": "XMLHttpRequest"
    }

    next_max_id = "0"
    for i in range(1):
      url = INSTAGRAM_FOLLOWERS_TEMPLATE.substitute(account_id=INSTAGRAM_ACCOUNT_ID, next_max_id=next_max_id)
      print(f"FOLLOWER URL: {url}")
      
      r = requests.get(url=url, headers=headers)
      follower_response = r.json()

      followers = follower_response["users"]
      page_size = follower_response["page_size"]

      print(f"FOLLOWERS: {len(followers)}")
      print(f"PAGE SIZE: {page_size}")

      with open("./data/results_" + next_max_id + ".json", "w") as file:
        json.dump(follower_response, file)

      if "next_max_id" in follower_response:
        next_max_id = follower_response["next_max_id"]
        print(f"NEXT MAX ID: {next_max_id}")
      else:
         print("No more records. Exiting")
         break;

      print("SLEEPING 2 SECONDS")
      time.sleep(2)

      # check if next_mad_id exist.  if not, no more entries

if __name__ == '__main__':
    main()
