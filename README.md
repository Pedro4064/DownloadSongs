# YouTube .mp3 Downloader
•Download all videos in a YouTube playlist as an mp3 file.<br/>
•Download all videos as .mp3 files from a csv file.<br/>
•Uses [yout.com](https://yout.com/) to download the files.

## [playlistURL.py ](playlistURL.py)
•Just enter the link for any video in the playlist, and the artist name, it will then gather all the videos' URLs and move to the yout website to start the download.

## [csvYoutube.py](csvYoutube.py)
•The option to read a csv file with the song info, and download.
•The csv file needs to have the folowing structure:
|Song Name|Artist|Youtube URL|
|---------|------|-----------|

*For an example see the [songs.csv](songs.csv)



## Python
#### Modules that need to be downloaded:<br/>

•[selenium](https://pypi.org/project/selenium/)<br/>
`python3.X pip install -u selenium`
## Chrome Driver

  •You also need to download [chromedriver](http://chromedriver.chromium.org/downloads) to use with selenium module.<br/> 
  *If you are on the raspberry pi, follow this [instructions](https://www.reddit.com/r/selenium/comments/7341wt/success_how_to_run_selenium_chrome_webdriver_on/). <br/>

## Notes
•You may need to change the path of the Downloads directory to fit the one on your machine: `os.chdir('/Users/pedrocruz/Downloads')`.<br/>
•You may need to change the path of the webDriver  to fit the one on your machine: `driverPath = '/Applications/chromedriver'`.<br/>
•To get the list of all files in the Downloads directory we use the `ls` bash command. You may need to change it if your OS is Windows.