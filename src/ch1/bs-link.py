# 라이브러리 읽어 들이기
from bs4 import BeautifulSoup

# 분석하고 싶은 html 
html = """
    <html><body>
        <ul>
            <li><a href="http://www.naver.com">naver</a></li>
            <li><a href="http://www.daum.com">daum</a></li>
        </ul>
    </body></html>
"""

# HTMl 분석
soup = BeautifulSoup(html, "html.parser")

# find_all() 메서드 추출
links = soup.find_all("a")

# 링크 목록 추출하기
for a in links:
    href = a.attrs['href']
    text = a.string
    print(text, ">", href)
