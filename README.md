# YouTube .mp3 Downloader
•Download all videos in a playlist as an mp3 file.<br/>
•Uses [yout.com](https://yout.com/) to download the files.

## YouTube 
•Just enter the link for any video in the playlist, and the artist name, it will then gather all the videos' URLs and move to the yout website to start the download.

## Python
•To download the modules:<br/>
`python -m pip install -r /path/to/requirements.txt`

## Notes
•You may need to change the path of the Downloads directory to fit the one on your machine: `os.chdir('/Users/pedrocruz/Downloads')`.<br/>
•You may need to change the path of the webDriver  to fit the one on your machine: `driverPath = '/Applications/chromedriver'`.<br/>
•To get the list of all files in the Downloads directory we use the `ls` bash command. You may need to change it if your OS is Windows.