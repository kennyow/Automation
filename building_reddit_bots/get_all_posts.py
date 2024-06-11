import praw
from datetime import datetime, timedelta

reddit = praw.Reddit(user_agent= True, client_id="6buSJ5p_1zO3LMSXbA7EBA", 
        client_secret="xgnZzT9m9iaSwcV1IEM5Est5TTJcrA", username="KennyoWEC", password="Kennyow86!"  )

subreddit = reddit.subreddit("conversas")

post24h = []
for post in subreddit.new():
    current_time = datetime.utcnow()
    post_time = datetime.utcfromtimestamp(post.created)
    #print(current_time, post_time)

    delta_time = current_time - post_time
    #print(delta_time)
    #Get the last 24h posts
    if delta_time <= timedelta(hours=24):
        post24h.append((post.title, post.selftext, post.created))

    
    print(post24h)