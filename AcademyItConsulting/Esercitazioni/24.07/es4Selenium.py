"""
Visita https://demoqa.com/dynamic-properties
Attendi che il bottone "Visible After 5 Seconds" appaia
Cliccalo e verifica che l'azione sia stata eseguita con successo
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def setup_driver():

    driver = webdriver.Chrome()
    return driver

def navigazione(driver):

    driver.get("https://demoqa.com/dynamic-properties")
    print(f"\nTitolo della pagina: {driver.title}")

    WebDriverWait(driver, 5).until( #il valore indica il tempo che aspetta prima di andare in errore
        EC.presence_of_element_located((By.ID, "visibleAfter"))
    )

    bottone = driver.find_element(By.ID, "visibleAfter")
    bottone.click()
    time.sleep(1)
    print("\nPulsante atteso e cliccato correttamente! ", "\nNome Bottone: ", bottone.text, "\n")

driver = setup_driver()
navigazione(driver)

