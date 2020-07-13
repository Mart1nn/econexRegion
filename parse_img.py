# import urllib
# import urllib.request
# from bs4 import BeautifulSoup
# import os
# from string import ascii_lowercase
# i=1
# def make_soup(url):
#     thepage= urllib.request.urlopen(url)
#     soupdata = BeautifulSoup(thepage, "html.parser")
#     return soupdata

# soup = make_soup("https://econex.ru/catalog/")
# for img in soup.findAll('img'):
#     temp=img.get('src')
#     if temp[:1]=="/":
#         image = "url here" + temp
#     else:
#         image = temp

#     print(image)

#     nametemp = img.get('alt')
#     if len(nametemp)==0:
#         filename=str(i)
#         i=i+1
#     else:
#         filename=nametemp


#     imagefile = open(filename + ".jpeg", 'wb')
#     imagefile.write(urllib.request.urlopen(image).read())
#     imagefile.close()


def grabimagetags():
import urllib2
from BeautifulSoup import BeautifulSoup
page = urllib2.urlopen('http://www.youtube.com/')
soup = BeautifulSoup(page)
tags = soup.findAll('img')
list.extend(set(tag['src'] for tag in tags))


return list