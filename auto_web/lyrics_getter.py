from ast import keyword
from click import option
from numpy import product
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import re
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def lyrics(keyword):
    lst=[]

    # url = ''
    
    # urlss=request.POST.get("urls")
    options=Options()
    options.headless=False
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')         
    # time.sleep(15)
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

    # chrome='E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe'
    # driver = webdriver.Chrome('/home/msy/WORK/NEWESCOUT/ESCOUT/chromedriver',options=options)
    # driver = webdriver.Chrome('E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe',chrome_options=options)
    # url="view-source:"+urlss
    # time.sleep(10)
    driver.switch_to.default_content()

    driver.get(keyword)
    # driver.get("https://matchlyric.com/onlybino-my-way/")

    # driver.find_element_by_xpath('//*[@id="q"]').send_keys(keyword)
    singer_name=driver.find_element_by_xpath('//*[@id="lyrics-details"]/div[3]/h1/div[3]').text
    song_name=driver.find_element_by_xpath('//*[@id="lyrics-details"]/div[3]/h1/div[2]').text
    
    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'lxml')
    # soup=BeautifulSoup()
    # reviews_selector = soup.find_all('div', class_='reviewSelector')

    productDivs = soup.find_all('div', attrs={'id' : 'kj-lyric-content'})
    # i=0
    lyric_lst=[]
    for result in productDivs:  
        name = result.find_all('p')
        # a=''.join(name.find('br').next_siblings)
        for i in name:
            if i.find('br').next_siblings:
                b=i.find('br').next_siblings
                c='\n'.join(map(str, b))
            
        # print(len(name))
        # for i in name:
        #     print(1)
            lyric_lst.append(c)
            # print(i.text)
            # print(lyric_lst)
    return lyric_lst,singer_name,song_name
    

        
# print(lyrics(1))
