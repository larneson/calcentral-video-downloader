# Calcentral Video Downloader

This is a script I made because I was tired of manually clicking on a bunch of course video links and I wanted to watch them offline sometimes. It opens up CalCentral and downloads all the videos from your current classes into your downloads folder. I might or might not maintain this or update it if it's useful to people.

## Installation
To download this you can clone it from here or download the zip. If you have a mac, installing the dependencies should be painless, just execute all the commands in the code boxes below. I don't know about Windows or Linux because I haven't tried it.

### Python
This project is in python 3. To download python follow these instructions from the [python website](https://www.python.org/downloads/). Or, since we're at Berkeley, you can read the instructions from [CS 61A](https://cs61a.org/lab/lab00/). (Which will also teach you about command line things if you don't already know.)

### Dependencies
This project makes use of several open source python libraries. To run the code you need selenium, BeautifulSoup4 and youtube_dl installed on your system. The easiest way is using pip, which comes with comes with python but you can find more instructions [here](https://pip.pypa.io/en/stable/installing/#upgrading-pip)
Then in the command line run
```
pip install selenium
pip install bs4
pip install youtube_dl
```
Or you can read how to do it on their individual websites:
selenium: http://selenium-python.readthedocs.io/installation.html
bs4: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup
youtube_dl: https://github.com/rg3/youtube-dl

Also, selenium requires a driver to run the web browser. I used PhantomJS because it doesn't open a physical browser, but you can use [any of the ones selenium supports](http://selenium-python.readthedocs.io/installation.html#drivers), just replace the line that says PhantomJS with your driver of choice. To install PhantomJS follow [this link](http://phantomjs.org/download.html), or if you're on mac like me you can just run
```
brew install phantomjs
```

### Cookies

Since most youtube class videos are login-restricted, we have to get around this using cookies.
You will need a method of downloading your cookies into a text file. I recommend [this chrome extension](https://chrome.google.com/webstore/detail/cookiestxt/njabckikapfpffapmjgojcnbfjonfjfg?hl=en). Log in with your calnet id and pull up one of the restricted youtube videos in your browser. Verify that it can play, then click on the cookies.txt plugin and copy the cookies from that page. Paste that into the cookies.txt file in the same directory as your python script. Note that now you have to do this every time your CalCentral login cookies expire, which is around 15 minutes or so. I am currently working on a way to fix this so it will do it automatically.

## Running
Replace "YOUR USERNAME HERE" and "YOUR PASSWORD HERE" with your CalNet ID and password respectively.
To run the script go into your terminal, navigate to this directory and run
```
python download.py
```
(or ```python3``` if that's your thing).
You can run this multiple times as the semester goes by and only videos that aren't in your Downloads folder will download. Note that if you delete videos this does mean that they'll re-download, so if you're low on disk space watch out. I might put in an option for only downloading newer videos at some point, but check out the youtube-dl documentation if you want to do that yourself (and open up a pull request :D).

### Customization

If you're on windows you might have to change the output file destination. Or you just might want to edit where the videos go. Change the first part of the line ```'~/Downloads/%(title)s.%(ext)s'``` to reflect the appropriate output location. Also check out youtube-dl's site if you want more options for downloading.
The link that includes ```fall-2017``` will also need to be replaced once a semester.

## Licence

Feel free to use this, change it, whatever, just credit me. But please only use it for personal use because Cal and YouTube don't like you stealing their videos!
