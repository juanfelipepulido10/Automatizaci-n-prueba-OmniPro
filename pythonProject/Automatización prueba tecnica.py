from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.mercadolibre.com.co/')
time.sleep(2)
Busqueda = driver.find_element_by_id('cb1-edit')
Busqueda.send_keys("BMW SERIE 3")
Busqueda.send_keys(Keys.ENTER)
time.sleep(5)
driver.close()

