# unfollow-x

A small Twitter utility project for identifying accounts that do not follow you back.

## Overview

This repository contains two Python scripts:

- `unfollow.py` — uses Tweepy with OAuth1 credentials to fetch your following and follower lists, then unfollow accounts that are not following you back.
- `unfollow_2.py` — uses the newer Tweepy client with a bearer token to fetch the same lists and print the number of accounts not following you back. It does not perform any unfollow actions.

## Requirements

- Python 3.10+ (or a compatible Python 3 version)
- Twitter developer credentials
- `tweepy`
- `python-dotenv`

Install dependencies from `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

## Setup

Create a `.env.local` file in the project root with the credentials required by the script you want to run.

### `unfollow.py`

```env
api_key=YOUR_API_KEY
api_secret=YOUR_API_SECRET
access_token=YOUR_ACCESS_TOKEN
access_token_secret=YOUR_ACCESS_TOKEN_SECRET
```

### `unfollow_2.py`

```env
BEARER_TOKEN=YOUR_BEARER_TOKEN
```

> Note: `unfollow_2.py` currently uses a hard-coded `my_id` value. Update the `my_id` variable in the script to match your own Twitter user ID.

## Usage

### Check who is not following you back

```bash
python unfollow_2.py
```

### Unfollow accounts that are not following you back

```bash
python unfollow.py
```

`unfollow.py` asks for confirmation before performing any unfollow actions.

## Caution

- Be careful when using automated unfollow scripts; Twitter rate limits and account rules may apply.
- Always verify your credentials and test on a secondary account if needed.

## Notes

- `unfollow.py` uses OAuth1 and writes unfollow actions.
- `unfollow_2.py` currently only reports accounts not following you back.
- Update `my_id` in `unfollow_2.py` before running if it does not match your Twitter user ID.
