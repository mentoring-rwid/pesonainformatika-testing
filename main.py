import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



def test_website():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    url = "https://pesonainformatika.com/belajar-python/"
    driver.get(url)
    
    entry_content = driver.find_element(By.CSS_SELECTOR, 'div.entry-content')
    links = entry_content.find_elements(By.CSS_SELECTOR, 'a')
    for link in links:
       driver.switch_to.new_window()
       t=driver.window_handles[-1]# Get the handle of new tab
       driver.switch_to.window(t)
       driver.get(link.get_attribute('href'))
       time.sleep(2)
       
    
    
if __name__ == "__main__":
    test_website()