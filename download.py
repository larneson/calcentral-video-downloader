#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import youtube_dl
from bs4 import BeautifulSoup
#import argparse
import os
import selenium.common.exceptions
from config import *

calcentral_url = 'https://auth.berkeley.edu/cas/login?service=https%3A%2F%2Fcalcentral.berkeley.edu%2Fauth%2Fcas%2Fcallback%3Furl%3Dhttps%253A%252F%252Fcalcentral.berkeley.edu%252Facademics'

sleep_time = 2

youtube_links = []
browser = webdriver.Chrome()
logged_in = False
courses = []

while not youtube_links and sleep_time < 20:
    try:
        browser.get(calcentral_url)
        if not logged_in:
            print("logging in...")
            time.sleep(sleep_time)
            username = browser.find_element_by_id("username")
            password = browser.find_element_by_id("password")
            username.send_keys(USERNAME)
            password.send_keys(PASSWORD)
            browser.find_element_by_name("submit").click()
            logged_in = True

        #get links for current classes
        print("getting current classes...")
        time.sleep(sleep_time)

        html = browser.page_source
        courses = []
        soup = BeautifulSoup(html, 'lxml')
        for link in soup.findAll('a'):
            url = link.get('href')
            if url and '/academics/semester/' + SEMESTER + '/class/' in url:
                courses.append(url)

        #find youtube links in class page
        for course in courses:
            youtube_links.append([])
            print("collecting youtube links for class", course)
            course_url = 'https://calcentral.berkeley.edu' + course
            browser.get(course_url)
            time.sleep(sleep_time)

            html = browser.page_source
            soup = BeautifulSoup(html, 'lxml')
            for link in soup.findAll('a'):
                url = link.get('href')
                if url and 'youtube' in url and link not in youtube_links:
                    youtube_links[-1].append(url)
        if not youtube_links or max([len(links) for links in youtube_links]) == 0:
            print("sleeptime too smol")
            sleep_time *= 2

    except selenium.common.exceptions.NoSuchElementException: # time too short error
        print(sleep_time," too short")
        sleep_time *= 2
        continue

if not youtube_links:
    print("no youtube links found")
    browser.quit()
    exit()

# getting cookies for youtube
print('logging in to youtube...')
browser.get('https://accounts.google.com/ServiceLogin')
time.sleep(sleep_time)
username = browser.find_element_by_id("identifierId")
username.send_keys(USERNAME + '@berkeley.edu')
browser.find_element_by_id("identifierNext").click()
time.sleep(sleep_time)
print("getting youtube cookies from browser...")
browser.get(youtube_links[0][0])
time.sleep(sleep_time)
with open('cookies.txt', 'w') as f:
    lines = ['# HTTP Cookie File']
    for cookie in browser.get_cookies():
        domain = cookie['domain']
        flag = "TRUE"
        path = cookie['path']
        secure = "TRUE" if cookie['secure'] else "FALSE"
        expiration = str(int(cookie.get('expiry', time.time() + 14 * 24 * 3600)))
        name = cookie['name']
        value = cookie['value']
        line = '\t'.join([domain, flag, path, secure, expiration, name, value])
        lines.append(line)
    f.write('\n'.join(lines))
browser.quit()

print("reading youtube links")
if os.path.exists('link_cache'):
    with open('link_cache', 'r') as f:
        cached = f.read().split('\n')
        for class_links in youtube_links:
            class_links = [l for l in class_links if l not in cached]


#download youtube links
print("downloading ", youtube_links)
if not OUTPUT_LOCATION:
    OUTPUT_LOCATION = 'lecture_videos/'





for i, class_links in enumerate(youtube_links):
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': OUTPUT_LOCATION + '/' + courses[i].split("/")[-1] + '/' + '%(title)s.%(ext)s', #gets last line of courses list, which is the class name
        'cookiefile': 'cookies.txt'
    }
    if LIMIT_RATE:
        ydl_opts['limit-rate'] = LIMIT_RATE
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(class_links)

print("writing completed youtube links")
with open('link_cache', 'w') as f:
    f.write('\n'.join(cached + youtube_links))
