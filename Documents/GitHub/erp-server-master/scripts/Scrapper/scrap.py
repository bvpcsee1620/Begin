from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

def getLinks(_soup):
    soup = _soup
    table = soup.find("table")
    links = table.findAll('a')
    data = []
    for link in links:
    	data.append([link['href'], link.get_text()])
    return data

def getImageUrl(_soup):
    soup = _soup
    table = soup.find("table")
    links = table.findAll('img')
    data = []
    for link in links:
    	data.append(link['src'])
    return data



url = [
	'http://cse.bvcoend.ac.in/site/home/index/228',
	'http://as.bvcoend.ac.in/site/home/index/293',
	'http://ice.bvcoend.ac.in/site/home/index/287',
	'http://eee.bvcoend.ac.in/site/home/index/269',
	'http://it.bvcoend.ac.in/site/home/index/357'
	]

for i in range(len(url)):
	print(url[i])
	soup = BeautifulSoup(requests.get(url[i]).content)

	profile = getLinks(soup)
	image = getImageUrl(soup)

	for j in range(len(profile)):
		profile[j].append(image[j])

	df = pd.DataFrame(columns=['profile_link', 'name', 'profile_photo_url'])
	for j in range(len(profile)):
		df.loc[j] = profile[j]
	df.to_csv('test{0}.csv'.format(i), index=False)