from bs4 import BeautifulSoup
import urllib.request as req

url = "https://ko.wikipedia.org/wiki/%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

# #mw-content-text 바로 아래에잇는
# ul > li > a태그 모두
a_list = soup.select(" #mw-content-text > div.mw-content-ltr.mw-parser-output > ul:nth-child(56) > li:nth-child(5) > a:nth-child(1)")
print(a_list)

for a in a_list:
    name = a.string
    print("-", name)
    
