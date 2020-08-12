import re
import urllib.request
url = 'https://en.wikipedia.org/wiki/Snake'
uf = urllib.request.urlopen(url)
html = uf.read()

soup = BeautifulSoup(html, 'html.parser')
for p in soup.find_all('p'):
    p = re.sub(r'\[[^\[\]]+\]', '', p.get_text())
    print(p + "\n")
