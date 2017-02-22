#coding=utf8
from bs4 import BeautifulSoup
import urllib
import json
from sys import argv

try:
    hashtag = argv[1]
except:
    hashtag = "sport"

page = urllib.urlopen(("https://www.instagram.com/explore/tags/%s/" % (hashtag)))
soup = BeautifulSoup(page,"lxml")
scripts = soup.find_all("script")
preparing_json = None
for s in scripts:
    if s.string:
        if "window._sharedData" in s.string:
            preparing_json = s.string


preparing_json = preparing_json[:-1]
preparing_json = preparing_json.replace("window._sharedData = ","")
preparing_json = json.loads(preparing_json)
tag = preparing_json["entry_data"]["TagPage"]
count = tag[0]["tag"]["media"]
count = count["count"]
print str(count) + "  Публикаций"