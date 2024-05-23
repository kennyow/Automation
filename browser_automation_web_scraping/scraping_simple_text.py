from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


#* SCRAPING THE PHRASE OF THE SITE
#* INITIALIZING SELENIUM
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
  driver.get(r'http://automated.pythonanywhere.com')
  return driver

def main():
  driver = get_driver()
  element = driver.find_element(by="xpath",value='/html/body/div[1]/div/h1[1]')
  return element.text



print(main())