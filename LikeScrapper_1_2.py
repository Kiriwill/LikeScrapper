from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

import sqlite3 as sql

#deactivate head and browser notification
options = Options()
options.set_headless(True)
options.set_preference("dom.webnotifications.enabled", False)
browser = webdriver.Firefox(options=options)

#set parameters to sqlite
cnc = sql.connect('Links.db')
c = cnc.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Links(link TEXT)")


likesList = []
n = 0

#get link from facebook
def get_links():
    browser.get("https://www.facebook.com")
    browser.find_element_by_name("email").send_keys("USERNAME")
    browser.find_element_by_name("pass").send_keys("PASS")
    browser.find_element_by_id("loginbutton").click()
    browser.get("https://www.facebook.com/INSERTPAGENAMEHERE/settings/?tab=people_and_other_pages")
    time.sleep(4)

    for link in browser.find_elements_by_xpath('//a[@data-hovercard]'):
        if (link == browser.find_elements_by_xpath('//a[@data-hovercard]')[100]):
            break
        else:
            likesList.append(link.get_attribute('href'))
            c_data()

#insert data into database
def c_data():
    global n

    while(n < len(likesList)):
        c.execute("INSERT INTO Links(link) VALUES(?)", ([likesList[n]]))
        cnc.commit()
        n+=1

#update data = not used but useful
def update():
        c. execute("UPDATE links SET link='Digite o Erro' WHERE link='Digite o local'")
        cnc.commit()

get_links()
c.close()
cnc.close()
