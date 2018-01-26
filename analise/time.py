
import os

os.chdir(r'C:\Users\rsilva\Google Drive\projects\programming\automation')

import datetime as dt
from time import sleep
from selenium.webdriver.common.by import By
from functions import *
import random




url = "http://sistemasnet/sarh/horarioflexivelNovo/lancamento/LancamentoHoras.asp?SISQSmodulo=18384"



def leave(time):


    while time > dt.datetime.now():

        print(dt.datetime.now())

        sleep(60 * random.randint(5,10))

    page = init_browser(webdriver=webdriver.Firefox())

    page.driver.get(url)

    btn = page.wait_for_element_to_click((By.ID, 'image2'))

    btn.click()

    alert = page.alert_is_present(timeout=5)

    alert.accept()

    sleep(5)

    try:

        alert = page.alert_is_present(timeout=5)

        alert.dismiss()

        sleep(5)

        page.close()

    except:

        print("Entered Except Block!")



def enter(time):

    while time > dt.datetime.now():

        print(dt.datetime.now())

        sleep(60 * random.randint(5, 10))

    page = init_browser(webdriver=webdriver.Firefox())

    page.driver.get(url)

    btn = page.wait_for_element_to_click((By.ID, 'image1'))

    btn.click()

    try:

        sleep(2)

        alert = page.alert_is_present(timeout=5)

        alert.dismiss()

    except:

        pass

    try:

        sleep(2)

        page.close()

    except:

        pass



entra = dt.datetime(2018, 1, 25, 9)

#sai = dt.datetime(2018, 1, 22, 20, 22)

#leave(sai)

enter(entra)

