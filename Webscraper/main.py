from selenium import webdriver # controls the webpage
from selenium.webdriver.common.by import By # helps locate elements on the webpage
from selenium.webdriver.common.keys import Keys # simulates user inputs
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager    # automatically installs the correct Chrome driver
import time # manages time
import json

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized") #opens chrome in full screen
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#opens linkedIn
driver.get('https://www.linkedin.com/login')
time.sleep(2)

with open("./config.json") as cred:
    config = json.load(cred)

username = config("linkedin_email")
password = config("linkedin_password")

email_input = driver.find_element(By.ID,"username")
email_input.send_keys(username)

password_input = driver.find_element(By.ID,"password")
password_input.send_keys(password)

login_button = driver.find_element(By.XPATH,"//button[@type='submit']")
login_button.click()

input("Press enter after entering in your authentication code")
