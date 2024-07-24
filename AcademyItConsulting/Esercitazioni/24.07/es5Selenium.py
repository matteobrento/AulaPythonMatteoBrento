"""
Visita https://news.ycombinator.com/
Estrai i titoli, i link e i punteggi dei primi 3 articoli
Salva questi dati in un file CSV
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time


def setup_driver():

    driver = webdriver.Chrome()
    return driver

def scraping(driver):

    driver.get("https://news.ycombinator.com/")

    title = driver.find_elements(By.CLASS_NAME, "titleline")
    link = driver.find_elements(By.CLASS_NAME, "sitestr")
    punti = driver.find_elements(By.CLASS_NAME, "score")

    lista_titoli = []
    lista_link = []
    lista_punti = []

    for t, l, p in zip(title[0:3], link[0:3], punti[0:3]):
        print(f"{t.text}, {l.text}, {p.text}")

    for titolo in title[0:3]:
        lista_titoli.append(titolo.text)

    for link_articolo in link[0:3]:
        lista_link.append(link_articolo.text)

    for punto in punti[0:3]:
        lista_punti.append(punto.text)

    driver.quit()

    return lista_titoli, lista_link, lista_punti

    

def crea_dataset():

    driver = setup_driver()
    lista_titoli, lista_link, lista_punti = scraping(driver)

    data = {
        "Titolo":lista_titoli,
        "Link":lista_link,
        "Punti":lista_punti
    }

    df = pd.DataFrame(data)
    print("DataFrame ottenuto dallo scriping: \n", df, "\n")
    df.to_csv("C:\\Users\\matte\\AcademyItConsulting\\Esercitazioni\\24.07\\Scraping_Articoli.csv", index=False)


crea_dataset()

