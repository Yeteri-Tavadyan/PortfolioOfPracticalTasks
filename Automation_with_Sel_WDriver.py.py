from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

print("START TESTING")

def browser_func(driver):
    driver.maximize_window()

    main_url = "https://www.python.org/"
    driver.get(main_url)

    driver.find_element("id", "id-search-field").send_keys("bla bla")
    time.sleep(2)
    driver.find_element("id", "submit").click()
    time.sleep(2)

    result = driver.find_element("css selector", "ul > p")
    print("Search result is:",  result.text)
    if result.text == "No results found.":
        print(True)
    else:
        print(False)

    page_title = driver.title
    print("Page title is:", page_title)
    current_url = driver.current_url
    print("Current URL is:", current_url)

    driver.close() 

browsers = ["chrome", "firefox"]
for x in browsers:
    if x == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        browser_func(driver)
        print("Testing ended in the Chrome browser. Wait for Firefox browser testing.")
    elif x == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        browser_func(driver)
        print("Testing ends in Firefox browser.")

print("TESTING ENDED IN BOTH BROWSERS!") 
       