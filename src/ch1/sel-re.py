from bs4 import BeautifulSoup
import re

html = """
    <ul>
        <li><a href="hoge.html">hoge</a></li>
        <li><a href="https://example.com/fuga">fuga*</a></li>
        <li><a href="https://example.com/foo">foo*</a></li>
        <li><a href="http://example.com/aaa">aaa</a></li>
    </ul>
"""

soup = BeautifulSoup(html, "html.parser")
# 정규표현식으로 href에서 https인 것 추출하기
li = soup.find_all(href=re.compile(r"^https://"))
for e in li:
    print(type(e.attrs), e.attrs)
    print(e.attrs['href'])