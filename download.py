from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import youtube_dl
from bs4 import BeautifulSoup

USERNAME = "YOUR USERNAME HERE"
PASSWORD = "YOUR PASSWORD HERE"

calcentral_url = 'https://auth.berkeley.edu/cas/login?service=https%3A%2F%2Fcalcentral.berkeley.edu%2Fauth%2Fcas%2Fcallback%3Furl%3Dhttps%253A%252F%252Fcalcentral.berkeley.edu%252Facademics'
browser = webdriver.PhantomJS()

try:
    browser.get(calcentral_url)

    #log in
    username = browser.find_element_by_id("username")
    password = browser.find_element_by_id("password")

    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)

    browser.find_element_by_name("submit").click()

    #get links for current classes
    time.sleep(5)

    html = browser.page_source
    courses = []
    soup = BeautifulSoup(html, 'lxml')
    for link in soup.findAll('a'):
        url = link.get('href')
        if url and '/academics/semester/fall-2017/class/' in url:
            courses.append(url)

    #find youtube links in class page
    youtube_links = []
    for course in courses:
        course_url = 'https://calcentral.berkeley.edu' + course
        browser.get(course_url)
        time.sleep(5)

        html = browser.page_source
        soup = BeautifulSoup(html, 'lxml')
        for link in soup.findAll('a'):
            url = link.get('href')
            if url and 'youtube' in url and link not in youtube_links:
                youtube_links.append(url)
    browser.quit()

    #download youtube links
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': '~/Downloads/%(title)s.%(ext)s',
        'cookiefile': 'cookies.txt'

    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(youtube_links)

finally:
    browser.quit()
