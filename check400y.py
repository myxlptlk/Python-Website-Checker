# importing the requests library 
import requests 
import time
from os import listdir
from os.path import isfile, join


def get_first(iterable, default=None):
    if iterable:
        for item in iterable:
            return item
    return default

# Import Files
file = ["site1Rewrites","site2Rewrites"]
urlPrefix = ["site1","site2"]
i = 1
while i < len(file):
  with open(file[i]) as fp:
    with open('UrlResponses.csv', 'a') as resultFile:
      line = fp.readline()
      while line:
          url = urlPrefix[i]+line.rstrip().split("$")[0].split()[1]
          start = time.time()
          r = requests.get(url)
          resultFile.write(url + "," + str(r) + "," + str(time.time() - start) + "\n")
          print(url)
          line = fp.readline()
  i += 1