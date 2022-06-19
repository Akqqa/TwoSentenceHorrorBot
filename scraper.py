from dotenv import load_dotenv
import praw
import os

def setupScraper():
    load_dotenv()

    client = os.getenv('CLIENT_ID')
    secret = os.getenv('CLIENT_SECRET')
    agent = os.getenv('USER_AGENT')

    reddit = praw.Reddit(
        client_id=client,
        client_secret=secret,
        user_agent=agent,
    )

    return reddit

def randomPostTitle(reddit, subredditName):
    print("hi")
    post = reddit.subreddit(subredditName).random()
    print("bye")
    return post.title

def randomPostText(reddit, subredditName):
    post = reddit.subreddit(subredditName).random()
    return post.selftext 

if __name__ == "__main__":
    reddit = setupScraper()
    print(randomPostTitle(reddit, "twosentencehorror"))
    print(randomPostText(reddit, "twosentencehorror"))
