# scrapeRedditPython
Scrape Reddit with Python

How to get started:

This is what you will need to get started:

1) Python 3.x
2) An IDE (Interactive Development Environment) or a Text Editor (Like Jupiter)
3) These two Python packages installed: Praw, to connect to the Reddit API, and Pandas.
4) A Reddit account: https://www.reddit.com/login/

The Reddit API

You have to Create and App within Reddit. “Create an App” 
Go to : https://www.reddit.com/prefs/apps (click create app or create another app button at the bottom left)

Pick a name for your application (you can add a description)
Also make sure you select the “script” option and don’t forget to put http://localhost:8080 in the redirect uri field.

You can always check Praw documentation: https://praw.readthedocs.io/en/latest/getting_started/authentication.html#script-application

Hit create app and now you are ready to use the OAuth2 authorization to connect to the API and start scraping: Copy and paste your 14-characters personal.

We will be using only one of Python’s built-in modules, datetime, and two third-party modules: https://wiki.python.org/moin/UsefulModules
