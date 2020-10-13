import requests
import re
from bs4 import BeautifulSoup
result  = requests.get("https://rocketleague.tracker.network/profile/steam/teicho")
src = result.content
soup = BeautifulSoup(src, 'lxml')
tbl = soup.find(id = "season-13")
rank = tbl.find_all("table", class_ = "card-table items")

keys1 = [8,9,10,14,15,16,23,24,25,30,31,32] #first 4 ranks
keys2 = [8,9,10,14,15,16,23,24,25,30,31,32,40,41,42,46,47,48,54,55,56,61,62,63] #all 8 ranks

keys3 = [5,6,7,9,10,11,13,14,15,17,18,19]

ranks = [rank[0].find("tbody").text]
nranks = re.sub('\n+',',',ranks[0])

nranks = nranks.split(",")

yess = [None] * len(keys3)
n= 0
for i in keys3:
  yess[n] = nranks[i]
  n= n+1
print(yess)
