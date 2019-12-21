from bs4 import BeautifulSoup
import requests
import os
from os import listdir
from os.path import isfile, join

path = "SiteMaps"
if not os.path.exists(path):
    os.makedirs(path)

site = "site"
languages = ["country1-language","country2-language","country2-language"]
sitemaps = ["type1","type2","type3"]

siteMapList = []
for subsite in languages:
    for sitemap in sitemaps:
        countryList = []
        siteMapURL = site + "/" + subsite + "/sitemap-" + sitemap + ".xml"
        r = requests.get(siteMapURL)
        xml = r.text
        soup = BeautifulSoup(xml)
        sitemapTags = soup.find_all("loc")
        print(siteMapURL + " is requested")
        for sitemapvalue in sitemapTags:
            countryList.append(sitemapvalue.text)
        fileName = str(subsite) + "_" + str(sitemap) + ".txt"
        folder = os.path.join(path,subsite)
        if not os.path.exists(folder):
            os.makedirs(folder)
        file = os.path.join(folder,fileName)
        if os.path.exists(file):
            os.remove(file)
        with open(file, 'w') as f:
            for item in countryList:
                f.write(item + "\n" )
            print(file + " is written")