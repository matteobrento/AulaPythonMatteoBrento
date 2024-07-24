"""
Uno script per visitare Wikipedia, cerca "Python (programming language)" e stampare il primo paragrafo della pagina risultante.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def setup_driver():

    driver = webdriver.Chrome()
    return driver

def navigazione(driver):

    driver.get("https://www.wikipedia.org")
    search_bar = driver.find_element(By.NAME, "search")
    search_bar.clear()
    search_bar.send_keys("Python (programming language)" + Keys.RETURN)
    link = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[3]/div[4]/ul/li[1]/div/div[2]/div[1]/a')
    link.click()
    time.sleep(3)
    stampa = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[1]')
    print("Ricerca completata")
    print("Paragrafo: \n", stampa.text)
    driver.quit()

driver = setup_driver()
navigazione(driver)

