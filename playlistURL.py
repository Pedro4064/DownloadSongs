from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from termcolor import colored
import time
import os
import sys 

mainUrl = ''
songsUrl = [None]
elements = [None]
names = [None]
songsUrl = []
elements = []
names = []
number_of_songs = 0

driverPath = '/Applications/chromedriver'

def user():

    global mainUrl
    global number_of_songs

    os.system('clear')
    mainUrl = input('•The url for the first song in the playlist->')
    

def gatherLink():

    global mainUrl
    global number_of_songs
    global songsUrl
    global elements
    global names

    generalXpath = '//*[@id="wc-endpoint"]'
    
    # Web driver settings
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options,executable_path=driverPath)
    wait = WebDriverWait(driver,100000)

    # Go to the main url and wait until the element appears
    driver.get(mainUrl)
    firstItem = wait.until(ec.visibility_of_element_located((By.XPATH, generalXpath)))
    
    # Get a list of elements with that xpath
    elements = driver.find_elements_by_xpath(generalXpath)

    for element in elements:

        print(element.get_attribute("href"))
        
        # Clear the name
        name = element.text.replace('TV SIZE','').replace('\n','').replace('IwannalickMenatsFeet', '')
        for letter in name:

            if letter in '1234567890:▶':
                name = name.replace(letter,'')

        print(name)
        
        # Check if the video is available or blocked
        if 'blocked' in name:
            #If it is block, skip and go to the next itereation 
            continue
        else:
            # Add the titles to the names list
            names.append(name)
            # Add the links to the list 
            songsUrl.append(element.get_attribute("href"))
        

def download():
    youtUrl = ''
    
    


if __name__=='__main__':
    user()
    gatherLink()