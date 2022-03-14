#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from IPython.display import clear_output
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyperclip


# In[32]:


result = []

web = webdriver.Chrome(executable_path='/Users/jackie/Downloads/chromedriver')
urllist = ['']
web.get('https://www.artandwriting.org/gallery')
btn = web.find_element_by_xpath('//*[@id="nav-section"]/ul/li[2]') # navigates to the writing category
btn.click()

btn = web.find_element_by_xpath('//*[@id="gallery-categories"]/ul/li[1]/a/span[2]')
btn.click()

time.sleep(5)

index = 0
while True:
    divs = web.find_elements_by_class_name('overlay')
    
    try:
        divs[index].click()
    except IndexError or index == 16:
        break
    print(str(index+1) + " done")
    result.append(web.find_element_by_class_name('art-box').text)
    web.back()
    
    index += 1
    
btn = web.find_element_by_xpath('//*[@id="gallery-grid"]/section/div/div/a')
btn.click()

time.sleep(2)

index = 0
while True:
    divs = web.find_elements_by_class_name('overlay')
    
    try:
        divs[index].click()
    except IndexError or index == 12:
        break
    print(str(index+1) + " done")
    result.append(web.find_element_by_class_name('art-box').text)
    web.back()
    
    index += 1


# In[33]:


for item in result:
    print(item)


# In[ ]:




