from selenium import webdriver

url = 'https://www.gmail.com'
chrome_driver_location = 'F:\\Python Projects\\EmailAutomation\\utilities\\chromedriver'

driver = webdriver.Chrome(executable_path = chrome_driver_location)

driver.get(url)