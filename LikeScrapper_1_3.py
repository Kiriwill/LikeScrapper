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
c.execute("CREATE TABLE IF NOT EXISTS Links(link TEXT, likes TEXT)")


likesList = []
n = 0

#get link and likes from facebook
class LikeScrapper:
        def __init__(self):
                browser.get("https://www.facebook.com")
                browser.find_element_by_name("email").send_keys("USERNAME_HERE")
                browser.find_element_by_name("pass").send_keys("PASS_HERE")
                browser.find_element_by_id("loginbutton").click()

        def get_links(self):
                browser.get("https://www.facebook.com/NAMEOFPAGE/settings/?tab=people_and_other_pages")
                time.sleep(4)
                for link in browser.find_elements_by_xpath('//a[@data-hovercard]'):
                        if (link == browser.find_elements_by_xpath('//a[@data-hovercard]')[100]):
                                break
                        else:
                                likesList.append(link.get_attribute('href'))
                                insert_links()
        def get_likes():
                browser.get("LINKTO_PROFILE_HERE")
                #browser.find_element_by_...(IN PROGRESS)

"""                 c.execute("SELECT link FROM Links")
                #data = c.fetchone()
                for r in c.fetchall():
                        browser.get(r)
                        time.sleep(4) """

#insert data into database
def insert_links():
    global n

    while(n < len(likesList)):
        c.execute("INSERT INTO Links(link) VALUES(?)", ([likesList[n]]))
        cnc.commit()
        n+=1


LS = LikeScrapper()
LS.get_links()
LS.get_likes()

c.close()
cnc.close()
