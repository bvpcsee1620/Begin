from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
users = pd.read_csv('test.csv')


def getImageUrl(_soup):
    soup = _soup
    imgs = soup.findAll("img")
    for img in imgs:
        if "http://bvcoend.ac.in/images/" in img['src']:
            return img['src']
    return None

for i in range(len(users)):
    profile_url = users.loc[i, "PROFILE LINK"]
    val = None
    try:
        soup = BeautifulSoup(requests.get(profile_url).content, "lxml")
        val = getImageUrl(soup)
    except:
        if val is None:
            val = ''
    users.loc[i, "profile_photo_url"] = val
    print(getImageUrl(soup))
    if getImageUrl(soup) is None:
        print(profile_url)
users.to_csv("test1.csv")