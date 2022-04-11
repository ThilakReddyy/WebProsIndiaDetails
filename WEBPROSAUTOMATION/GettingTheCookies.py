import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC


def gettingthecookies(url,roll,passwod):
    DRIVER_PATH=os.path.dirname(__file__)+'\..\chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    ser = Service(DRIVER_PATH)
    driver=webdriver.Chrome(service=ser,options=options) #loading the chrome driver
    driver.get(url) #loading the url
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "txtId2")) )
    username = driver.find_element(By.NAME,'txtId2')
    username.send_keys(roll)
    password = driver.find_element(By.NAME,'txtPwd2')
    password.send_keys(passwod)
    driver.find_element(By.NAME,'imgBtn2').click()
    try:
        alert = Alert(driver)
        alert.accept()
    except:
        pass
    r=driver.get_cookies()
    driver.quit()
    return 'ASP.NET_SessionId='+r[1]['value']+'; frmAuth='+r[0]['value']