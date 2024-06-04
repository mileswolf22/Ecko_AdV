import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from comandos import Comandos
from hablar_voz import Voz_asistente

voz = Voz_asistente()
driver = webdriver.Chrome()

voz.hablar("Indique el comando")
comando = voz.transfromar_audio_en_texto()

if comando == "inciar navegador":
    driver.get("https://www.google.com")
    time.sleep(10)
    voz.hablar("Siguiente comnando")
    comando_2 = voz.transfromar_audio_en_texto()

    if comando_2 == "abrir youtube":
        driver.get("https://www.youtube.com")
        time.sleep(10)

"""search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)"""
