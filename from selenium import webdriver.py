from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
import openpyxl
import smtplib
import os
from email.message import EmailMessage
import re


# Inicializar o WebDriver (neste caso, Chrome)
driver = webdriver.Chrome()

# Abrir a página da web
driver.get('https://telefonesimportados.netlify.app/')

# Encontrar o elemento desejado (substitua pelo seu localizador)
elemento = driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div/div/h2')

# Obter o texto do elemento
texto_elemento = elemento.text

# Imprimir o texto do elemento no console
print("Texto do elemento:", texto_elemento)

# Fechar o navegador ao terminar
driver.quit()