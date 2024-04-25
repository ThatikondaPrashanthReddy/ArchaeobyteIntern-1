import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.bikewale.com/royalenfield-bikes/"
page = requests.get(url)


soup = BeautifulSoup(page.content,'html.parser')
print(soup.prettify)

#images
'''img1=[]
image=soup.findAll('div',class_="o-brXWGL o-frwuxB")
for i in image:
    j=i.img['src']
    img1.append(j)
print(img1)'''

#links
'''links=[]
link=soup.findAll('div',class_='o-fznJEv o-bTDyCI o-brXWGL')
for i in link:
    j=i.a['href']
    links.append(j)
print(links)'''

#text
links=[]
link=soup.findAll('div',class_='o-fznJEv o-bTDyCI o-brXWGL')
for i in link:
    j=i.a.text
    links.append(j)
print(links)

#using csv we have to store the data
'''with open('imglink.csv','w') as csv_file:
    write=csv.writer(csv_file)
    write.writerow(image)
    for i in image:
        j=i.img['src']
        img1.append(j)
    write.writerow(img1)'''


