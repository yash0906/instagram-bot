from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time


### for firefox
browser_profile = webdriver.FirefoxProfile()
browser_profile.set_preference("dom.webnotifications.enabled",False)
browser = webdriver.Firefox(firefox_profile = browser_profile)


### for chrome
# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications" : 2}
# chrome_options.add_experimental_option("prefs",prefs)
# browser = webdriver.Chrome(chrome_options=chrome_options)


browser.get('https://www.instagram.com/accounts/login/')
email_id = input("Enter your email: ")#'yashbhansali0906@gmail.com'
password  = input("Enter your password: ")#'Yash@0906'
print("entering your instagram----")
email = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
email.send_keys(email_id)
pwd = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
pwd.send_keys(password + Keys.ENTER)
print("----entered your instagram")


url = input("input the url ,whose posts you want to comment on: ")
# url = 'https://www.instagram.com/imsridhar/'
browser.get(url)
last_height = browser.execute_script("return document.body.scrollHeight")
while True:
	browser.execute_script("window.scrollTo(0,document.body.scrollHeight+200);")
	time.sleep(2)
	new_height = browser.execute_script("return document.body.scrollHeight")
	# print(new_height)
	if new_height == last_height:
		break
	last_height = new_height
photos = browser.find_elements_by_class_name("_9AhH0")
print("Number of posts: " + str(len(photos)))
k=0
msg = input("Enter your message: ")
for i in photos:
	k+=1
	i.click()
	time.sleep(2)
	comm = browser.find_element_by_class_name('Ypffh')
	comm.click()
	time.sleep(0.5)
	comm = browser.find_element_by_class_name("Ypffh")
	comm.send_keys(msg + '🤩😎🤩' + Keys.ENTER)
	time.sleep(4)
	close  = browser.find_element_by_xpath('/html/body/div[4]/button[1]')
	close.click()
	time.sleep(1)
	print(k)
browser.quit()