import tweepy
import time

import os
from dotenv import load_dotenv

load_dotenv(".env.local")

# Fill in your credentials from the developer portal
API_KEY = os.getenv("api_key")
API_SECRET = os.getenv("api_secret")
ACCESS_TOKEN = os.getenv("access_token")
ACCESS_TOKEN_SECRET = os.getenv("access_token_secret")

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

me = api.verify_credentials()
my_id = me.id
print(f"My ID is: {me.id}")
print(type(my_id))
print(f"Logged in as: {me.screen_name}")

print("Fetching following list...")
following = set()
for user in tweepy.Cursor(api.get_friend_ids, user_id=my_id).items():
    following.add(user)

print("Fetching followers list...")
followers = set()
for user in tweepy.Cursor(api.get_follower_ids, user_id=my_id).items():
    followers.add(user)

not_following_back = following - followers
print(f"\nFound {len(not_following_back)} accounts not following you back.")

confirm = input("Proceed to unfollow all? (yes/no): ")
if confirm.lower() != "yes":
    print("Aborted.")
else:
    for i, user_id in enumerate(not_following_back):
        try:
            api.destroy_friendship(target_id=user_id)
            print(f"Unfollowed user ID: {user_id} ({i+1}/{len(not_following_back)})")
            time.sleep(1)  # Avoid hitting rate limits
        except tweepy.TweepyException as e:
            print(f"Error unfollowing {user_id}: {e}")

    print("Done!")