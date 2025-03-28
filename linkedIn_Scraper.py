from selenium import webdriver # controls the webpage
from selenium.webdriver.common.by import By # helps locate elements on the webpage
from selenium.webdriver.common.keys import Keys # simulates user inputs
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager    # automatically installs the correct Chrome driver
import time
import json
import convenient_lists
import convenient_methods


#closes browser
def scraper_log_out(driver):
    driver.close()
    return

# Opens browser, logs into linked in
# Also creates the Raw Data folders, etc
def scraper_log_in():
    convenient_methods.create_folders()
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized") #opens chrome in full screen
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
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
    return driver

# Searches the webpage using various key spots in the HTML of linkedIn's page.
# Pulls the text out of HTML and stores it to a JSON file, originally keeping the HTML code
# and the text in general using a Selenium built in. 

def search_and_scrape(search , post_total,driver):
    
    time.sleep(3)
    search_input = driver.find_element(By.XPATH,"//input[@placeholder='Search']")
    time.sleep(1)
    search_input.click()
    time.sleep(1)
    search_input.send_keys(search)
    time.sleep(1)
    search_input.send_keys(Keys.RETURN)
    time.sleep(5)

    posts_button = driver.find_element(By.XPATH, "//button[contains(@class, 'search-reusables__filter-pill-button')]")
    # checking if the posts button has been clicked or not.
    if posts_button.get_attribute("aria-pressed") != "true":        
        posts_button.click()
        time.sleep(3)
   
   
    posts_data  = set()

    while len(posts_data) < post_total:
        post_elements = driver.find_elements(By.CLASS_NAME, "feed-shared-update-v2__description")
        for post in post_elements:
            # added try catch from a chat gpt recommendation during my code review
            try:
                post_text = post.text
                post_html = post.get_attribute('outerHTML')
                posts_data.add((post_html,post_text))
            
            except Exception as e:
                print(f"Error while scraping post: {e}")
            
            time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
   
    posts_data = [{"post_html": html, "post_text": text} for html,text in posts_data]    
    with open(f'Raw_Data/{search}.json','a', encoding='utf-8') as json_file:
        json.dump(posts_data, json_file, ensure_ascii=False, indent=4)
        
    print(f'Scrape successful? {len(posts_data)} posts saved to {search}.json')
    driver.refresh()
    time.sleep(2)
    search_input = driver.find_element(By.XPATH,"//input[@placeholder='Search']")
    search_input.clear()
    time.sleep(3)
    return

if __name__ == "__main__":
    driver = scraper_log_in()
    for search in convenient_lists.search_list:
        search_and_scrape(search,10)
        print(f'{search} complete!')
    scraper_log_out(driver)