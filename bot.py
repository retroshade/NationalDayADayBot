import tweepy

from secrets import *
from bs4 import BeautifulSoup
import urllib

# auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
# auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
# api = tweepy.API(auth)

# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# """

url = urllib.urlopen('https://nationaldaycalendar.com/latest-posts/').read()

soup = BeautifulSoup(url, 'html.parser')
print(soup.prettify())

# api.update_status(tweet)