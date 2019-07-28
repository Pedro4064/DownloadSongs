from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


import subprocess
import time
import os
import sys 

# Add the path for the MacProgressbar module
sys.path.append('/Users/pedrocruz/Desktop/Programming/Python/Git/MacProgressBar')
from MacProgressBar import ProgressBar


mainUrl = ''
artist = ''
remove = ''
nameOfChannel = ''
songsUrl = [None]
elements = [None]
names = [None] 
songsUrl = []
elements = []
names = []


# Web driver settings
driverPath = '/Applications/chromedriver'
# options = Options()

# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options,executable_path=driverPath)
driver = webdriver.Chrome(executable_path=driverPath).minimize_window()
wait = WebDriverWait(driver,100000)

def user():

    global mainUrl 
    global artist
    global remove
    global nameOfChannel


    mainUrl = input('•The url for the first song in the playlist->')
    artist = input('•The artist->')
    remove = input('•Part of the titles you wish to remove->')
    nameOfChannel = input('•Name of channel->')
    

def gatherLink():

    global mainUrl
    global songsUrl
    global elements
    global names
    global driver
    global remove
    global nameOfChannel
    

    generalXpath = '//*[@id="wc-endpoint"]'
    
    # Go to the main url and wait until the element appears
    driver.get(mainUrl)
    firstItem = wait.until(ec.visibility_of_element_located((By.XPATH, generalXpath)))
    
    # Get a list of elements with that xpath
    elements = driver.find_elements_by_xpath(generalXpath)

    for element in elements:

        # Clear the name (remove the name of the channel that always appears on the element.rxr)
        name = element.text.replace('TV SIZE','').replace('\n','').replace(nameOfChannel,'')
        name = name.replace(remove,'')

        for letter in name:

            if letter in '1234567890:▶-':
                name = name.replace(letter,'')

        print(name)
        
        # Check if the video is available or blocked
        if 'blocked' in name:
            #If it is block, skip and go to the next itereation 
            continue

        else:

            # Clean the rawUrl-> so the url is just the video's, and not the playlist
            rawUrl = element.get_attribute("href")
            rawUrl = rawUrl.split('&')
            url = rawUrl[0]
            
            # Add the titles to the names list
            names.append(name)
            # Add the links to the list 
            songsUrl.append(url)
        

def download():

    global driver 
    global names 
    global songsUrl
    global artist

    # Change to the download directory
    os.chdir('/Users/pedrocruz/Downloads')

    youtUrl = 'https://yout.com/'
    inputXpath = '/html/body/div[1]/div/div/div/div[1]/form/div/input'
    nameXpath = '/html/body/div[2]/div/div[1]/div/div[2]/div[3]/div[3]/div[3]/div/input'
    artistXpath = '/html/body/div[2]/div/div[1]/div/div[2]/div[3]/div[3]/div[4]/div/input'
    recordXpath = '/html/body/div[2]/div/div[1]/div/div[2]/div[3]/div[3]/div[5]/button'
    Download = False

    # Creates the ProgressBar instance
    progressBar = ProgressBar(max = len(songsUrl)+1,message='Starting Download',style = 'seven eighths')
    # Go to that website 
    driver.get(youtUrl)
    # Wait until the input box loads
    inputBox = wait.until(ec.visibility_of_element_located((By.XPATH, inputXpath)))

    # Goes through all the links and type the url in the input box
    for url,name in zip(songsUrl,names):
        
        # Update the progressBar
        progressBar.next(message='Downloading '+name)
        # Types the link in the input box
        driver.find_element_by_xpath(inputXpath).send_keys(url)
        
        # Wait until the name box loads
        nameBox = wait.until(ec.visibility_of_element_located((By.XPATH, nameXpath)))

        # Clear the input box and Send the title of the song to the name box
        driver.find_element_by_xpath(nameXpath).clear()
        driver.find_element_by_xpath(nameXpath).send_keys(name)

        # Clear the input box and send the artist's name to the artist's input box
        driver.find_element_by_xpath(artistXpath).clear()
        driver.find_element_by_xpath(artistXpath).send_keys(artist)

        # Press the record button
        driver.find_element_by_xpath(recordXpath).click() 
        
        # Goes in loop to see if the file has been downloaded
        # Get the initial files in the Downloads directory, to compare it to future iterations
        lastLs = subprocess.check_output('ls')
        lastLs = lastLs.split()

        ls = []

        while Download == False:
            
            # Check again, if it is different from the first one, it means the file was added
            ls = subprocess.check_output('ls')
            ls = ls.split()

            if ls != lastLs:
                Download = True
            

            # for output in ls:

            #     print(name.replace(' ','').replace(',','').replace(' ','-')+'.mp3')
            #     if output == name.replace(',','').replace(' ','-')+'.mp3':
            #         Download = True
            #     else:
            #         pass

        # Update variables for next iteration
        Download = False
        ls = []
               

if __name__=='__main__':
    os.system('clear')
    print('\n\n')
    print("__   __         _____      _                             _____ \n\\ \\ / /__  _   |_   _|   _| |__   ___     _ __ ___  _ __|___ / \n \\ V / _ \\| | | || || | | | '_ \\ / _ \\   | '_ ` _ \\| '_ \\ |_ \\ \n  | | (_) | |_| || || |_| | |_) |  __/  _| | | | | | |_) |__) |\n  |_|\\___/ \\__,_||_| \\__,_|_.__/ \\___| (_)_| |_| |_| .__/____/ \n                                                   |_|         ")
    
    user()
    gatherLink()
    download()
    ProgressBar.next(message='Download Finished ♪')