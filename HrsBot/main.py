from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from file import Rohit as r

class spam1:
    def __init__(self, fname, lname, pnum, email):
        self.driver = webdriver.Chrome()
        self.driver.get('https://news.un.org/en/content/un-newsletter-subscribe')
        sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div[2]/section/section/section/div/div/div/div/div/div/form/div/div[2]/input').send_keys(email)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div[2]/section/section/section/div/div/div/div/div/div/form/div/div[4]/input').send_keys(lname)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div[2]/section/section/section/div/div/div/div/div/div/form/div/div[3]/input').send_keys(fname)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div[2]/section/section/section/div/div/div/div/div/div/form/div/div[7]/div[1]/div/div[2]/ul/li[2]/label').click()
        sleep(10)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div[2]/section/section/section/div/div/div/div/div/div/form/div/div[10]/input').click()
        sleep(10)

spam1(r.fname, r.lname, r.pnum, r.email)