# Alberto Davila Lab 10 -- BS4
from bs4 import BeautifulSoup
from urllib.request import urlopen

htmlFile = 'C:\\Users\\apiod\\Downloads\\GoodReads.html'
'''
url = 'https://www.goodreads.com/list/show/143500.Best_Books_of_the_Decade_2020_s'
html  = urlopen(url)
soup = BeautifulSoup(html,'html.parser')

with open (htmlFile,'w',encoding='utf8') as file:
    file.write(soup.prettify())
'''

with open (htmlFile,'r',encoding='utf8') as file:
    html = file.read()
    soup = BeautifulSoup(html,'html.parser')
booklist = []
books = soup.find_all(itemtype="http://schema.org/Book")
for book in books:
    book = soup.find(itemtype="http://schema.org/Book")
    titletag = book.find(class_='bookTitle')
    title = titletag.get_text().strip()

    authortag = book.find(class_="authorName")
    author = authortag.get_text().strip()

    bookinfo = [title, author]
    booklist.append(bookinfo)

print(booklist)
