from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time


#* AUTOMATE LOGIN PROCESS

def get_driver():
  #Set options to make browser easier
  options = webdriver.ChromeOptions()
  options.add_argument('disable-infobars')
  options.add_argument('start-maximized')
  options.add_argument('disable-dev-shm-usage')
  options.add_argument('no-sandbox')
  options.add_experimental_option('excludeSwitches', ['enable-automation'])
  options.add_argument('disable-blink-features=AutomationControlled')
  
  
  driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
  driver.get(r'http://automated.pythonanywhere.com/login/')
  return driver

def main():
  driver = get_driver()
  driver.find_element(by="id",value='id_username').send_keys("automated")
  time.sleep(2)
  driver.find_element(by="id",value='id_password').send_keys("automatedautomated" + Keys.RETURN) #Keys.RETURN gives the Enter
  print(driver.current_url) # Gets the current URL(in case, https://automated.pythonanywhere.com/dashboard/)
  
  #*CLICK HOME BUTTON
  driver.find_element(by="xpath" , value = '/html/body/nav/div/a').click() 
  time.sleep(2)
  print(driver.current_url)

print(main())