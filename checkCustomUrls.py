# importing the requests library 
import requests 
import time
import os
import datetime
from os import listdir
from os.path import isfile, join


def get_first(iterable, default=None):
    if iterable:
        for item in iterable:
            return item
    return default

# Import Files
directory = './SiteMaps'
URLRequestResutlsFile = "URLRequestResults.csv"
listofurls = []
timestamp = datetime.datetime.now()

for url in listofurls:
    with open("URLRequestResultsSite.csv", 'a+', encoding="utf-8") as f:
        start = time.time()
        try:
            r = requests.get(url)
        except requests.exceptions.RequestException:
            f.write(url + " ; TIMEOUT ; " + str(time.time() - start) + "\n")
            continue
        f.write(url + " ; " + str(r) + " ; " + str(time.time() - start) + "\n")