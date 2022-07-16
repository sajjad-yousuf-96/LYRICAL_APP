# from ast import keyword
# from click import option
# from numpy import product
from selenium import webdriver
from bs4 import BeautifulSoup as bs
# import pandas as pd
import re
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from lyrics_getter import lyrics
from selenium import webdriver
import chromedriver_autoinstaller

def mainpage():
    lst=[]

    url = 'https://matchlyric.com'
    
    # urlss=request.POST.get("urls")
    options=Options()
    options.headless=False
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')         
    # time.sleep(15)
    # driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=options)
    # chrome='E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe'
    # driver = webdriver.Chrome('/home/msy/WORK/NEWESCOUT/ESCOUT/chromedriver',options=options)
    # driver = webdriver.Chrome('E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe',chrome_options=options)
    # url="view-source:"+urlss
    # time.sleep(10)
    # driver.switch_to.default_contsent()

    driver.get(url)
    # driver.find_element_by_xpath('//*[@id="q"]').send_keys(keyword)
    # driver.find_element_by_xpath('//*[@id="topActionHeader"]/div/div[2]/div/div[2]/form/div/div[2]/button').click()
    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'lxml')
    # soup=BeautifulSoup()
    # reviews_selector = soup.find_all('div', class_='reviewSelector')

    data = soup.findAll('td', attrs={'class' : 'tsong'})
    for td in data:
        # for div in td:
        b=td.find('a')['href']
        lst.append(b)
    lst=lst[5::]
    return lst
    # print(lst)
    # print(len(lst))
    # total=0
    # for i in lst:
    #     lyrics(i)
    #     total=total+1
    #     # if total == 1:
    #     #     break



# mainpage()