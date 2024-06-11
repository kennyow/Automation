import praw
from datetime import datetime, timedelta

reddit = praw.Reddit(user_agent= True, client_id="6buSJ5p_1zO3LMSXbA7EBA", 
        client_secret="xgnZzT9m9iaSwcV1IEM5Est5TTJcrA", username="KennyoWEC", password="Kennyow86!"  )

subreddit = reddit.subreddit("corrida")

for post in subreddit.new():
    current_time = datetime.utcnow()
    post_time = datetime.utcfromtimestamp(post.created)
    delta_time = current_time - post_time
    if delta_time <= timedelta(month=2):
        if "Tenis Iniciante" in post.title.lower():
            post.reply("Recomendo o Corre 3")

        # post24h.append((post.title, post.selftext, post_time))
        # file.write(f'{post.title}\n{post.selftext}\n\n')