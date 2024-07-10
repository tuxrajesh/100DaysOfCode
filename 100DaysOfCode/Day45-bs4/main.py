from bs4 import BeautifulSoup

with open("website.html") as fle:
    contents = fle.read()
    
soup = BeautifulSoup(contents, "html.parser")
all_anchor =  soup.find_all(name="a")
for tag in all_anchor:
    print(tag.get("href"))