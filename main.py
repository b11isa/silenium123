from selenium import webdriver
import time
import os
url = "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"
a = requests.get(url)
text = BeautifulSoup(a.text, 'html.parser')
a = text.body.p.textprint(a)
df = pd.DataFrame({'Name': [a]})
df.to_excel('teams.xlsx')
a = webdriver.Chrome()
a.get("https://www.google.com")
time.sleep(5)
os.system(r'c:\Users\IsroilB\PycharmProjects\httpproject\teams.xlsx')

