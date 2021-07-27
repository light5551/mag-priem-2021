import requests
from bs4 import BeautifulSoup

r = requests.get("https://etu.ru/ru/abiturientam/priem-v-magistraturu/podavshie-zayavlenie/ochnaya/byudzhet/programmnaya-inzheneriya")
soup = BeautifulSoup(r.text)
print(soup.prettify())
table = soup.find("table").find_all("tr")
for man in table:
    for td in man.find_all("td"):
        print(td)
        #print(td.get_text())
