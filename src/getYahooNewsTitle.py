import requests;
from bs4 import BeautifulSoup;
import re;

def main():
    url = 'https://news.yahoo.co.jp/'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html)

    # <a> のタグに対して hrefで正規表現でhttps://news.yahoo.co.jp に一致する範囲のタグをすべてリストで取り出す
    for a in soup.find_all('a', {'href': re.compile(url)}):
        new_title = a.text
        link = a['href']
        print(new_title, link)

if __name__ == "__main__":
    main()