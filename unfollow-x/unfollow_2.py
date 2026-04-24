import tweepy
import os
import time
from dotenv import load_dotenv

load_dotenv(".env.local")

BEARER_TOKEN = os.getenv("BEARER_TOKEN")

client = tweepy.Client(bearer_token=BEARER_TOKEN)

my_id = 1656507871

print("Fetching following list...")

following = set()
response = client.get_users_following(id=my_id, max_results=1000)

while response:
    if response.data:
        for user in response.data:
            following.add(user.id)

    if "next_token" in response.meta:
        response = client.get_users_following(
            id=my_id,
            pagination_token=response.meta["next_token"],
            max_results=1000
        )
    else:
        break

print("Fetching followers list...")

followers = set()
response = client.get_users_followers(id=my_id, max_results=1000)

while response:
    if response.data:
        for user in response.data:
            followers.add(user.id)

    if "next_token" in response.meta:
        response = client.get_users_followers(
            id=my_id,
            pagination_token=response.meta["next_token"],
            max_results=1000
        )
    else:
        break

not_following_back = following - followers
print(f"\nFound {len(not_following_back)} accounts not following you back.")