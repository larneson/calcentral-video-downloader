# Calcentral Video Downloader

This is a script I made because I was tired of manually clicking on a bunch of course video links and I wanted to watch them offline sometimes. It opens up CalCentral and downloads all the videos from your current classes into a folder of your choice. I might or might not maintain this or update it if it's useful to people.

## Installation
To download this you can clone it from here or download the zip. If you have a mac, installing the dependencies should be painless, just execute all the commands in the code boxes below. I don't know about Windows or Linux because I haven't tried it.

### Python
This project is in python 3. To download python follow these instructions from the [python website](https://www.python.org/downloads/). Or, since we're at Berkeley, you can read the instructions from [CS 61A](https://cs61a.org/lab/lab00/). (Which will also teach you about command line things if you don't already know.)

### Dependencies
This project makes use of several open source python libraries. To run the code you need selenium, BeautifulSoup4, lxml, and youtube_dl installed on your system. The easiest way is using pip, which comes with comes with python but you can find more instructions [here](https://pip.pypa.io/en/stable/installing/#upgrading-pip).

There is a requriements.txt file with the libraries.To install all the libraries (but not chromedriver), in the calcentral-video-downloader directory run
```
pip install -r requirements.txt
```

Alternatively, in  command line run
```
pip install selenium
pip install bs4
pip install lxml
pip install youtube_dl
```
Or you can read how to do it on their individual websites:  
selenium: http://selenium-python.readthedocs.io/installation.html  
bs4: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup  
youtube_dl: https://github.com/rg3/youtube-dl

Also, selenium requires a driver to run the web browser. I used Chrome because the cookies got kind of messed up for different ones.
```
brew install chromedriver
```
if you're on mac else install here:
https://sites.google.com/a/chromium.org/chromedriver/downloads

## Running
Replace "YOUR USERNAME HERE" and "YOUR PASSWORD HERE" in config.py with your CalNet ID and password respectively.
To run the script go into your terminal, navigate to this directory and run
```
python download.py
```
(or ```python3``` if that's your thing).
You can run this multiple times as the semester goes by and only videos that aren't in your Downloads folder will download. Note that if you delete videos this does mean that they'll re-download, so if you're low on disk space watch out. I might put in an option for only downloading newer videos at some point, but check out the youtube-dl documentation if you want to do that yourself (and open up a pull request :D).

### Customization

If you want to edit where the videos go, change the variable ```OUTPUT_LOCATION``` in config to reflect the appropriate output location. Also check out youtube-dl's site if you want more options for downloading.
The link that includes ```fall-2017``` will also need to be replaced once a semester.

## Licence

Feel free to use this, change it, whatever, just credit me. But please only use it for personal use because Cal and YouTube don't like you stealing their videos!

## TODO
- automatically hide chromedriver window
- make sure to get links for all classes
- only download new videos
- ask for username/password if not in config
- add -v options, etc
