from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
ser = Service(r"C:\Users\rosha\Downloads\chromedriver\chromedriver.exe")
website = 'https://www.careerguide.com/career-options'

#open the browser
driver = webdriver.Chrome(service=ser)

#load the webpage
driver.get(website)

#scaping text for actuary, techer and engineer
actuary = driver.find_element(By.LINK_TEXT, 'Actuary')
print(actuary.text)

teacher = driver.find_element(By.LINK_TEXT, "School Teacher")
print(teacher.text)

engineer = driver.find_element(By.LINK_TEXT, "Automobile Engineer")
print(engineer.text)
#driver.quit()
