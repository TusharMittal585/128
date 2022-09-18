from bs4 import BeautifulSoup as bs
import pandas as pd
import requests 

START_URL='https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
page=requests.get(START_URL)
#print(page) 
soup=bs(page.text,'html.parser')  
Star_table=soup.find('table')
temp_list=[]
table_reuse=Star_table.find_all('tr')
for tr in table_reuse:
    td=tr.fid_all('td') 
    row=[i.text.rstrip()for i in td] 
    temp_list.append(row) 
star_name=[]
star_mass=[]
star_distance=[]
star_radius=[]
star_lum=[]
for i in range (1,len(temp_list)):
    star_name.append(temp_list[i][1])
    star_distance.append(temp_list[i][3])
    star_mass.append(temp_list[i][5])
    star_radius.append(temp_list[i][6])
    star_lum.append(temp_list[i][7])

df2=pd.DataFrame(list(zip(star_name,star_radius,star_distance,star_lum,star_mass)),columns=['star_name','star_radius','star_mass','star_distance','star_lum'])
print(df2) 
df2.to_csv('bright_stars.csv') 