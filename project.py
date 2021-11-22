
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import csv


bright_stars_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(bright_stars_url)

soup = bs(page.text,'html.parser')

star_table = soup.find('table')

temp_list= []
table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.strip() for i in td]
    temp_list.append(row)



Star_names = []
Distance =[]
Mass = []
Radius =[]
Lum = []
final =[]

for i in range(1,len(temp_list)):
    
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7])
    

final = list(zip(Star_names,Distance,Mass,Radius,Lum))
print(final)


with open("finalstarsnew.csv", "w") as f:
        csvwriter = csv.writer(f)
        #csvwriter.writerow(headers)
        csvwriter.writerows(final)  