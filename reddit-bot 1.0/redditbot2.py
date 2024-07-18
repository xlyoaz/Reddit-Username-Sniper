import praw
import itertools
import time

# Reddit API credentials
client_id = ''
client_secret = ''
user_agent = ''
username = ''
password = ''

# Create a Reddit client
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password
)

# Characters to check for usernames
characters = 'abcdefghijklmnopqrstuvwxyz0123456789-_'
length = 3

# Create a list to store unavailable usernames
unavailable_usernames = []

# Open the file to write unavailable usernames
with open('unavailable_usernames.txt', 'w') as file:
    for combination in itertools.product(characters, repeat=length):
        username = ''.join(combination)
        try:
            # Check if the username exists
            reddit.redditor(username).id
            print(f"Username taken: {username}")
        except praw.exceptions.RedditAPIException as e:
            print(f"API Error: {str(e)}")
            time.sleep(5)  # Delay before retrying in case of an API error
        except praw.exceptions.PRAWException as e:
            print(f"PRAW Error: {str(e)}")
            unavailable_usernames.append(username)
            file.write(username + '\n')
        except Exception as e:
            print(f"Other Error: {str(e)}")
            unavailable_usernames.append(username)
            file.write(username + '\n')
        time.sleep(1)  # Delay to avoid hitting API rate limit

print("Process completed. Unavailable usernames saved to 'unavailable_usernames.txt'.")
