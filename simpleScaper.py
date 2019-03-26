#simple web scraper
#takes first 10 stories from technewsworld.com
#3/14/19
from bs4 import BeautifulSoup
import urllib

newList = []
newList2 = []
newList3 = []
numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
string1 = "http://www.technewsworld.com"

#use a predetermined website
r = urllib.urlopen('http://www.technewsworld.com/').read()	

#use the soup library
soup = BeautifulSoup((r),"html.parser")

#look through div elements for date and 
all_dates=soup.find_all("div", class_="date")
all_links=soup.find_all("a", class_="story-link")


test = soup.select('.title > a[href]')


for title in test[:10]:
	newList.append(title.text)
for date in all_dates[:10]:
	newList2.append(date.string)
for link in all_links[:10]:
	newList3.append(string1 + link.get("href"))

#combine all the elements together to print in a semi readable format
for k, x, y, z in zip(numberList, newList, newList2, newList3):
	print k, "-", x, "-", y, "-", z