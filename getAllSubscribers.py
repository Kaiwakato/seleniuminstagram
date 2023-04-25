from selenium import webdriver

from selenium.webdriver.common.by import By

import time

browser = webdriver.Firefox()

link = "https://www.instagram.com/"

browser.get(link)

time.sleep(2)

username = browser.find_element(By.NAME,"username")
password = browser.find_element(By.NAME,"password")

link_username = "yourusername"
link_password = "yourpassword"

username.send_keys(link_username)
password.send_keys(link_password)

loginButton = browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]/button")

loginButton.click()

time.sleep(5)

not_now = browser.find_element(By.CSS_SELECTOR,"._a9--._a9_1")

not_now.click()

time.sleep(7)

browser.get(link + link_username + "/")

time.sleep(5)

buttons = browser.find_elements(By.CSS_SELECTOR,".xl565be.x2pgyrj.x1m39q7l.x1uw6ca5")

followersButton = buttons[1]

followersButton.click()

time.sleep(5)

jscommand= """
followers = document.querySelector("._aano");
followers.scrollTo(0,followers.scrollHeight);
var lenOfPage=followers.scrollHeight;
return lenOfPage;
"""

lenOfPage = browser.execute_script(jscommand)
match = False
while(match == False):
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match = True
time.sleep(5)

followersList = []

followers = browser.find_elements(By.CSS_SELECTOR,".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.notranslate._a6hd")

for follower in followers:
    followersList.append(follower.text)

with open("followers.txt","w",encoding = "UTF-8") as file:
    for follower in followersList:
        file.write(follower + "\n")

browser.close()
