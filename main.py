#coding=utf8
from bs4 import BeautifulSoup
import urllib
import json
from operator import itemgetter
from sys import argv




def parser(hashtag):
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
    return count,hashtag


try:
    filename = argv[1]
    file = open("%s" % filename,"r")
except:
    file = open("tags.txt","r")
record = open("answer.txt","w")

tags = file.read()
tags = tags.split("\n")
tags = tags[:-1]

tags = [parser(i) for i in tags ]

tags = sorted(tags,key=lambda x: x[0], reverse=True)

for i,j in tags:
    print str(i) +' '+ j
    record.write(str(i) +' '+ j+'\n')

record.close()