from bs4 import BeautifulSoup

with open("./fruits-vegetables.html", encoding="utf-8")  as fp:
    soup = BeautifulSoup(fp, "html.parser")
    
# CSS 선택자 추출
#print(soup.select_one("li:nth-of-type(8)").string)
print(soup.select_one("#ve-list > li:nth-of-type(4)").string)
print(soup.select("#ve-list > li[data-lo='us']")[1].string)
print(soup.select("#ve-list > li.black")[1].string)

# find 메서드 추출
cond = {"data-lo": "us", "class": "black"}
print(soup.find("li", cond).string)
print(soup.find(id="ve-list").find("li", cond).string)