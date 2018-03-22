from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
path_to_chromedriver = r"D:\vit\web mining\project\chromedriver.exe" #path where chrome driver is stored
browser = webdriver.Chrome(path_to_chromedriver)
browser.get('https://www.facebook.com/pg/vituniversity/reviews/') #url from where you want to scrap
posts=browser.find_elements_by_class_name("text_exposed_root")
file1=open("D:/vit/web mining/project11/abc.txt","a") #path where you want to store the scrapped data in text file
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(10)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(10)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(10)
h=browser.find_elements_by_tag_name('p')
for h1 in h:
	file1.write(h1.text)
	file1.write("\n")
file1.close()