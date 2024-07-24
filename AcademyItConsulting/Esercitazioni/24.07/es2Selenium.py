"""
Visita https://practicetestautomation.com/practice-test-login/
Effettua il login con username "student" e password "Password123"
Verifica che il login sia avvenuto con successo
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def setup_driver():

    driver = webdriver.Chrome()
    return driver

def navigazione(driver):

    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(1)
    search_bar_username = driver.find_element(By.NAME, 'username')
    search_bar_username.clear()
    search_bar_username.send_keys('student' + Keys.RETURN)
    time.sleep(1)
    search_bar_psw = driver.find_element(By.NAME, 'password')
    search_bar_psw.clear()
    search_bar_psw.send_keys('Password123' + Keys.RETURN)
    time.sleep(1)
    tasto_subtmit = driver.find_element(By.ID, 'submit')
    tasto_subtmit.click()
    time.sleep(1)
    stampa = driver.find_element(By.XPATH, '/html/body/div/div/section/div/div/article/div[2]/p[1]/strong')
    if driver.title == "Logged In Successfully | Practice Test Automation":
        print("Login eseguito correttamente!", stampa.text)
    else:
        print("Login errato!")
    driver.quit()

driver = setup_driver()
navigazione(driver)