from selenium import webdriver # controls the webpage
from selenium.webdriver.common.by import By # helps locate elements on the webpage
from selenium.webdriver.common.keys import Keys # simulates user inputs
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager    # automatically installs the correct Chrome driver
from selenium.webdriver.common.action_chains import ActionChains
import time # manages time
import json

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized") #opens chrome in full screen
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


search_list = [
    'resumetips',
    'resume tips',
    'jobsearch',
    'Resume Writing Tips',
    'Data Analysis Interviews',
    'what languages to learn in data',
    'data skills',
    'interviewtips'
]

#opens linkedIn
def scraper_log_in(driver):
    driver.get('https://www.linkedin.com/login')
    time.sleep(2)

    with open("config.json") as cred:
        config = json.load(cred)

    username = config["linkedin_email"]
    password = config["linkedin_password"]

    email_input = driver.find_element(By.ID,"username")
    email_input.send_keys(username)

    password_input = driver.find_element(By.ID,"password")
    password_input.send_keys(password)

    login_button = driver.find_element(By.XPATH,"//button[@type='submit']")
    login_button.click()
    return


def search_and_scrape(search,post_total):
    time.sleep(2)
    actions = ActionChains(driver)
    search_input = driver.find_element(By.XPATH,"//input[@placeholder='Search']")
    time.sleep(1)
    search_input.send_keys(search)
    time.sleep(1)
    search_input.send_keys(Keys.RETURN)
    time.sleep(5)

    posts_button = driver.find_element(By.XPATH,"//*[@id='search-reusables__filters-bar']/ul/li[1]/button")
    posts_button.click()
    time.sleep(3)

    post_elements = driver.find_elements(By.CLASS_NAME, "feed-shared-update-v2__description")
    posts_data  = []

    while len(posts_data) < post_total:
        for post in post_elements:
            # added try catch from a chat gpt recommendation during my code review
            try:
                post_text = post.text
                post_html = post.get_attribute('outerHTML')

                posts_data.append({'post_html': post_html,
                                'post_text': post_text})
            
            except Exception as e:
                print(f"Error while scraping post: {e}")
            time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        
    with open(f'{search}.json','w', encoding='utf-8') as json_file:
        json.dump(posts_data, json_file, ensure_ascii=False, indent=4)
        
    print(f'Scrape successful! {len(posts_data)} posts saved to {search}.json')
    return

scraper_log_in(driver)

search_and_scrape('Resume Tips',20)


#for search in search_list:
#    search_and_scrape(search)
