from urllib import request
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

URL='https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page=requests.get(URL)
soup=bs(page.text,'html.parser') 

star_table=soup.find_all("table")

temp_list=[]

table_rows=star_table[7].find_all("tr") 

for tr in table_rows:
    td=tr.find_all("td")
    rows=[i.text.rstrip()for i in td] 
    temp_list.append(rows)

star_names=[]
star_distance=[]
mass=[]
radius=[]

for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][0])
    star_distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])
 
df2=pd.DataFrame(list(zip(star_names,star_distance,mass,radius)),columns=['star_names','star_distance','mass','radius'])
print(df2) 
df2.to_csv('dwarf_stars.csv')  