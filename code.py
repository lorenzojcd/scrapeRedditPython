#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id='PERSONAL_USE_SCRIPT_14_CHARS', \
                     client_secret='SECRET_KEY_27_CHARS ', \
                     user_agent='YOUR_APP_NAME', \
                     username='YOUR_REDDIT_USER_NAME', \
                     password='YOUR_REDDIT_LOGIN_PASSWORD')
					 
#We will use the subreddit r/Nootropics
					 
subreddit = reddit.subreddit('Nootropics')

top_subreddit = subreddit.top()

top_subreddit = subreddit.top(limit=500)

for submission in subreddit.top(limit=1):

#scrape this information about the topics: title, score, url, id, number of comments, date of creation, body text.

    print(submission.title, submission.id)
	
	topics_dict = { "title":[], \
                "score":[], \
                "id":[], "url":[], \ 
                "comms_num": [], \
                "created": [], \
                "body":[]}
				
for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)
	
	
#The data
	
topics_data = pd.DataFrame(topics_dict)