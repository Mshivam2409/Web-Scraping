import requests
import urllib.request
import time
from bs4 import *
import pandas
url = str(input("Enter the url:"))
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
names = []
project = []
org = []
result = soup.findAll('div', attrs = {'class':'md-padding archive-project-card__header archive-project-card__header--mod-0'}) 
for res in result:
    i = 0
    for divs in res.findChildren('div'):
        if i%2==0:
            project.append(divs.text)
        else:
            org.append(divs.text.split("Organization: ")[1])
        i = i + 1    
for res in result:
    names.append(res.h4.text.strip())
df = pandas.DataFrame(data={"Person Name": names, "Project": project,"Organization": org})
df.to_csv("./answer1.csv", sep=',',index=False)

