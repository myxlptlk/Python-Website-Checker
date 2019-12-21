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

for item in os.listdir(directory):
    subdirectory = os.path.join(directory,item)
    resultsFile = os.path.join(subdirectory,URLRequestResutlsFile)
    if os.path.exists(resultsFile):
        os.rename(resultsFile, resultsFile.replace(".csv",str(timestamp.day) + str(timestamp.month) + str(timestamp.year) + ".csv"))
    for fileitem in os.listdir(subdirectory):
        if(fileitem == "URLRequestResults.csv"):
            continue       
        with open(resultsFile, 'a+') as f:
            file = os.path.join(subdirectory,fileitem) 
            with open(file) as fp:
                line = fp.readline()
                while line:
                    url = line.rstrip()
                    start = time.time()
                    try:
                        r = requests.get(url+"?NondaBot")
                    except requests.exceptions.RequestException:
                        f.write(url + " ; TIMEOUT ; " + str(time.time() - start) + "\n")
                        continue
                    f.write(url + " ; " + str(r) + " ; " + str(time.time() - start) + "\n")
                    line = fp.readline()