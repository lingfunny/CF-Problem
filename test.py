from bs4 import BeautifulSoup
import re
from os import system
import requests

limit = -1 # 爬取 Round >= limit 的题目
url = 'https://codeforces.com/problemset/page/1?tags=constructive+algorithms,2200-2500'

# data = requests.get(url)
# f = open("codeforces.html", "w", encoding="utf-8")
# f.write(data.text)
# f.close()
f = open("caught.txt", "w", encoding="utf-8")

# soup = BeautifulSoup(data.text, 'lxml')

def prb(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

def TagF(href):
    return href and not re.compile("tags=").search(href) and not re.compile("submit").search(href) and not re.compile("status").search(href)
def TitleF(tag):
    return tag.has_attr('title') and tag['title'] == 'Difficulty'
def TagT(href):
    return href and re.compile("tags=").search(href)

dic = {}

lst = None

for page in range(1, 114514):
    url_ = re.sub("/[0-9]+", '/' + str(page), url)
    print("url: %s" % url_)
    newcontent = requests.get(url_).text
    print("Got!")
    if newcontent == lst:
        print("finished")
        system("pause")
        exit()
    else: lst = newcontent
    soup = BeautifulSoup(newcontent, 'lxml')
    for tag in soup.find_all(name = "tr"):
        # print(tag.prettify())
        s = tag.text
        s = re.sub("\s+", ' ', s)
        idx = re.findall("[0-9]+[A-Z][0-9]?", s)
        if not idx: continue
        if int(re.findall("[0-9]+", idx[0])[0]) < limit:
            print("finished")
            system("pause")
            exit()
        link = "https://codeforces.com/problemset/problem/%s/%s" % (re.findall("[0-9]+", idx[0])[0], re.findall("[A-Z]+[0-9]?", idx[0])[0])
        links = tag.find_all(name = "a", href = TagF)
        # print(links)
        # 0: ID
        # 1: NAME
        ID = re.sub("\s*", "", links[0].text)
        if dic.get(ID) != None:
            print("finished")
            system("pause")
            exit()
        print("ID: %s" % ID)
        NAME = re.sub("\s*", "", links[1].text)
        span = re.sub("\s*", "", tag.find_all(TitleF)[0].text)
        tags = []
        for tg in tag.find_all(name = "a", href = TagT):
            tags.append(tg.text)
        f.write("[%s. %s](%s) (\*%s)\ntags: %s\n\n" % (ID, NAME, link, span, ', '.join(tags)))
        dic[ID] = 1

    del soup
    del newcontent

f.close()