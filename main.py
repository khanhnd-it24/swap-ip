from turtle import update
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import requests
import time

link = "https://birdeye.so"
ant_input = "/html/body/div/div/div[2]/div/div[2]/div[1]/div[1]/div/span/input"
list_item = "/html/body/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div"

text = input("Enter text: ")

def doSomething():
    try: 
        driver = webdriver.Chrome(executable_path=r'D:\Work\chromedriver_win32\chromedriver.exe') # to open the chromebrowser 
        driver.get(link)
        time.sleep(25)
        driver.find_element_by_xpath(ant_input).send_keys(text)
        time.sleep(10)
        parrentDiv = driver.find_element_by_xpath(list_item)
        items = parrentDiv.find_elements_by_class_name("eLItHB")
        idx = 0
        for i in range(0, len(items)):
            if(items[i].text == text):
                idx = i
                break

        items[idx].click()
        time.sleep(20)
        driver.delete_all_cookies()
        driver.close()
    except:
        driver.delete_all_cookies()
        driver.close()
        doSomething()

def checkIp():
    try:
        public_ip = requests.get("http://wtfismyip.com/text").text
        print(public_ip)
    except:
        checkIp()

dem = 1
while True:
    doSomething()
    checkIp()
    print(dem)
    dem += 1
    time.sleep(10)

