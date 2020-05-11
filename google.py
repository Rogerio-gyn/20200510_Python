from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com.br")

print(driver.current_url)
print(driver.capabilities['browserVersion'])

element = driver.find_element_by_name("q")
element.click()
element.send_keys("Pyjamas conf")
element.submit()
print(driver.title)

assert driver.title == "Pyjamas conf - Pesquisa Google"


sleep(3)

driver.close()