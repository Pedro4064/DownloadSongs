from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


import subprocess
import time
import os
import sys 





songsUrl = [None]
artists = [None]
names = [None] 
songsUrl = []
artists = []
names = []


driverPath = '/Applications/chromedriver'

# Web driver settings
# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options,executable_path=driverPath)
driver = webdriver.Chrome(executable_path=driverPath)
wait = WebDriverWait(driver,100000)



def readCSV():

        
    global names 
    global songsUrl
    global artists


    os.system('clear')
    fileName = input('•The path to the csv File-> ')
    counter = 0

    with open(fileName,'r') as csv:
        
        for line in csv:

            # Skip first line(line with the titles for each column )
            if counter == 0:
                counter+=1
                continue
                
            # Split the line in columns 
            line = line.split(',')

            # Add each variable to the corresponding list 
            names.append(line[0])
            artists.append(line[1])
            songsUrl.append(line[2])
            print(line[0],line[1],line[2])

            # Update the counter
            counter+=1

def download():
    
    global driver 
    global names 
    global songsUrl
    global artists

    # Change to the download directory
    os.chdir('/Users/pedrocruz/Downloads')

    youtUrl = 'https://yout.com/'
    inputXpath = '/html/body/div[1]/div/div/div/div[1]/form/div/input'
    nameXpath = '/html/body/div[2]/div/div[1]/div/div[2]/div[3]/div[3]/div[3]/div/input'
    artistXpath = '/html/body/div[2]/div/div[1]/div/div[2]/div[3]/div[3]/div[4]/div/input'
    recordXpath = '/html/body/div[2]/div/div[1]/div/div[2]/div[3]/div[3]/div[5]/button'
    Download = False

    # Go to that website 
    driver.get(youtUrl)
    # Wait until the input box loads
    inputBox = wait.until(ec.visibility_of_element_located((By.XPATH, inputXpath)))

    # Goes through all the links and type the url in the input box
    for url,name,artist in zip(songsUrl,names,artists):

        print(name,artist,url)
        
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

if __name__ == "__main__":

    readCSV()    
    download()