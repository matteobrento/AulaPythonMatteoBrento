"""
Visita https://www.w3schools.com/html/html_tables.asp
Estrai i dati dalla prima tabella sulla pagina e stampali in formato leggibile
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup_driver():

    driver = webdriver.Chrome()
    return driver

def navigazione(driver):
    driver.get("https://www.w3schools.com/html/html_tables.asp")
    time.sleep(2)

    table_class = driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[1]/div[3]/div/table')
    tabella = driver.find_element(By.ID, 'customers')
    righe = tabella.find_elements(By.TAG_NAME, 'tr')    #tag name mi permette di utlizzare il tag html della riga
    
    for riga in righe[1:]:  #parto dalla riga dei valori escludendo l'intestazione
        celle = riga.find_elements(By.TAG_NAME, 'td')   #td è il tag dei valori in th
        """ 
        for cella in celle:
            valori = [cella.text] #me li stampa ad elenco
        """
        valori = [cella.text for cella in celle]   #me li stampa per riga della tabella in una lista
        print(valori)
    
    driver.quit()

driver = setup_driver()
navigazione(driver)