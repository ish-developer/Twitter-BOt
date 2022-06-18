import os
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

email = os.environ["email"]

password = os.environ["pass"]
twitter_id = input("What is your twitter id?")

service = Service(executable_path="C:/Users/ishme/OneDrive/Desktop/msedgedriver")
browser = webdriver.Edge(service=service)

browser.get("https://twitter.com/login")
time.sleep(10)

browser.maximize_window()

btn = browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div['
                                     '2]/div/div/div/div[5]/label/div/div[2]/div/input')

time.sleep(10)
a = ActionChains(browser)

time.sleep(10)
a.move_to_element(btn).perform()
time.sleep(5)

btn.send_keys(f"{email}")

time.sleep(7)

email_btn = browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                           '2]/div[2]/div/div/div/div[6]')
time.sleep(5)

a.move_to_element(email_btn).perform()

time.sleep(5)

a.click(email_btn).perform()

time.sleep(5)

pass_input = browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                            '2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')

a.move_to_element(pass_input).perform()

pass_input.send_keys(f"{twitter_id}")

next_btn = browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                          '2]/div[2]/div[2]/div/div/div')

a.move_to_element(next_btn).perform()

a.click(next_btn).perform()

time.sleep(5)

pass_input = browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                            '2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')

a.move_to_element(pass_input).perform()

pass_input.send_keys(f"{password}")

next_btn2 = browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                           '2]/div[2]/div[2]/div/div[1]/div/div')

a.move_to_element(next_btn2).perform()

a.click(next_btn2).perform()

time.sleep(5)

tweet_area = browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
                                            '2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                            '1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div['
                                            '2]/div/div/div/div')
a.move_to_element(tweet_area).perform()

tweet = input("Please Enter your tweet!!")

tweet_area.send_keys(tweet)

tweet_btn = browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
                                           '2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div')

a.move_to_element(tweet_btn).perform()

a.click(tweet_btn).perform()
