import praw

reddit = praw.Reddit(user_agent= True, client_id="6buSJ5p_1zO3LMSXbA7EBA", 
        client_secret="xgnZzT9m9iaSwcV1IEM5Est5TTJcrA", username="KennyoWEC", password="Kennyow86!"  )

url = "https://www.reddit.com/r/conselhodecarreira/comments/1dd0wju/me_ajudem_a_escolher_uma_faculdade_profiss%C3%A3o/"

post = reddit.submission(url=url)
print(post.title)
print(post.selftext)


print(len(post.comments))
for comment in post.comments:
    print(comment.body)