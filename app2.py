import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()  
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options,)
s= "dog"
url = (f"https://www.google.com/search?sca_esv=de788ad3f268e4d9&rlz=1C1RXQR_enIN1124IN1124&sxsrf=ADLYWIL7b3bo5kKXI47PwmH5ThEBS5wFrQ:1725284686025&q={s}&udm=2&fbs=AEQNm0BKxFXqFZETuC92mLOmXO9xJMdcEc6vsS8xotR_o6JIE4V6fjYfCiBijvGcXvcw0A1foGVwwGEV12VfBpqJrQOcY1lJEcwoWHBLO3iBa7iZ5QeKaux7sBp-0kIsG2kUeAyUyzSAO-CZcgzBYoFkfzufWRMKGShC9yzL_fiVgQjXh-cDB0Dw_GCPhaIOVi8Sfx8gJtP8O5qwqhDugIYu7nYGZD8J6w&sa=X&ved=2ahUKEwjS--KmsqSIAxUL7jgGHZ1kAKkQtKgLegQIGxAB&biw=1536&bih=703&dpr=1.25")
driver.get(url)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(5)

imgResults = driver.find_elements(By.TAG_NAME, 'img')
src = []

for img in imgResults:
    print(src.append(img.get_attribute('src')))
    for i in range(10):
        urllib.request.urlretrieve(str(src[i]),"sample_data/pets{}.jpg".format(i))