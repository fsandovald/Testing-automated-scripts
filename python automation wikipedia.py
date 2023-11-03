from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.google.com")

search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))

search_box.send_keys("automatización")
search_box.send_keys(Keys.RETURN)

wikipedia_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Wikipedia")))
wikipedia_link.click()

primer_proceso_automatico = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[33]')))
print(primer_proceso_automatico.text)

driver.save_screenshot("wikipedia.png")

driver.quit()
