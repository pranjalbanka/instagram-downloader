from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import requests

import time
import os 

# Your options
def scroll(driver, timeout):
    scroll_pause_time = timeout

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # If heights are the same it will exit the function
            break
        last_height = new_height

def all_links(url):
    # Setup the driver. This one uses firefox with some options and a path to the geckodriver
    driver = webdriver.Chrome()
    # implicitly_wait tells the driver to wait before throwing an exception
    #driver.implicitly_wait(3)
    # driver.get(url) opens the page
    driver.get(url)
    # This starts the scrolling by passing the driver and a timeout
    scroll(driver, 5)
    # Once scroll returns bs4 parsers the page_source
    soup_a = BeautifulSoup(driver.page_source, 'lxml')
    # Them we close the driver as soup_a is storing the page source
    # Empty array to store the links
    links = []
    posts_links=[]

    for link in soup_a.find_all('a'):
        # link.get('href') gets the href/url out of the a element
        if "https://www.picuki.com/media/" in link.get('href', ''):
            links.append(link.get('href'))

    posts_links = links

    directory = username
      
    # Parent Directory path 
    parent_dir = "/Users/pranjal/Desktop/"
      
    # Path 
    path = os.path.join(parent_dir, directory) 
      
    # Create the directory 
    # 'GeeksForGeeks' in 
    # '/home / User / Documents' 
    os.mkdir(path) 

    # Parent Directory path 
    sub_dir = "/Users/pranjal/Desktop/"+str(username)

    for i in range(1,len(posts_links)+1):
        sub_directory = str(i)
        path = os.path.join(sub_dir, sub_directory) 
        os.mkdir(path) 





    i=1
    j=len(posts_links)

    for link in posts_links:
        driver.get(link)
        video_links =[]
        images_list =[]
        try:
            videos = driver.find_elements_by_xpath("//source[@src]")
            images = driver.find_elements_by_xpath("//div[@class='item' or @class='single-photo']//img[@src]")
        except NoSuchElementException:  #spelling error making this code not work as expected
            pass

        for video in videos:

            if 'https://scontent' in video.get_attribute("src"):
                url=video.get_attribute("src")
                filename = "/Users/pranjal/Desktop/"+str(username)+"/"+str(j)+"/"+str(i)+".mp4"
                r = requests.get(url)
                i=i+1
                open(filename, 'wb').write(r.content)

        for image in images:

            if 'https://scontent' in image.get_attribute("src"):
                url=image.get_attribute("src")
                filename = "/Users/pranjal/Desktop/"+str(username)+"/"+str(j)+"/"+str(i)+".jpg"
                r = requests.get(url)
                i=i+1
                open(filename, 'wb').write(r.content)


        print(j)

        j=j-1

    driver.quit()

username = input("username : ")
all_links('https://www.picuki.com/profile/'+username)

