import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import logging 
import os

save_dir ="img/"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
query = "eprimat d"
response = requests.get(f"https://www.google.com/search?q={query}&sxsrf=AJOqlzUuff1RXi2mm8I_OqOwT9VjfIDL7w:1676996143273&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiq-qK7gaf9AhXUgVYBHYReAfYQ_AUoA3oECAEQBQ&biw=1920&bih=937&dpr=1#imgrc=1th7VhSesfMJ4M")    
soup=BeautifulSoup(response.content,'html.parser')
img_tag=soup.find_all("img" ,limit=50)

del img_tag[0]
img_data_list=[]
for i in img_tag:
    img_url=i['src']
    img_data= requests.get(img_url ).content
    my_dict={"image":img_url,"image":img_data}
    img_data_list.append(my_dict)
    with open(os.path.join(save_dir,f"{query}_{img_tag.index(i)}.jpg"),'wb') as f:
            f.write(img_data)