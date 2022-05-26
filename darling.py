from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
#chapter_number=2;
#main manga web site: https://darlinginthefranxx.com/
#base_url = "https://darlinginthefranxx.com/manga/darling-in-the-franxx-chapter-{}/".format(chapter_number)

base_url = 'https://darlinginthefranxx.com/manga/anime-name-chapter-1/'

driver.get(base_url)
#Uncomment the following two lines if you have slow internet
#import time
#time.sleep(20)

elements = driver.find_elements(By.CLASS_NAME,'separator a')

import wget
number = 1
for element in elements:
    url = element.get_attribute("href")
    #url = element.rstrip('"').lstrip('"')
    file_name = wget.download(url)
    print('Downloaded ',number)
    number+=1
print('Completed the downloads')

