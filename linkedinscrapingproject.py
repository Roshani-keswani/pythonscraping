from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
ser = Service(r"C:\Users\rosha\Downloads\chromedriver\chromedriver.exe")
website = "https://www.linkedin.com"

#open the browser
driver = webdriver.Chrome(service=ser)

#load the webpage
driver.get(website)
signin = driver.find_element(By.XPATH, "/html/body/nav/div/a[2]")
signin.click()

username = driver.find_element(By.XPATH, '//*[@id="username"]')
username.send_keys("roshanipradeepk@gmail.com")

password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys("roshniswati")

signin = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
signin.click()
time.sleep(0)
driver.get("https://www.linkedin.com/jobs/")
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3352110151&geoId=114806696&keywords=python&location=Pune%2C%20Maharashtra%2C%20India&refresh=true")
time.sleep(0)

def searchfor(title, loc):
    searchenter = driver.find_element(By.XPATH, '//*[@id="jobs-search-box-keyword-id-ember25"]')
    searchenter.clear()
    searchenter.send_keys(title)

    location = driver.find_element(By.XPATH, '//*[@id="jobs-search-box-location-id-ember25"]')
    location.clear()
    location.send_keys(loc)

    driver.find_element(By.XPATH, '//*[@id="global-nav-search"]/div/div[2]/button[1]').click()

searchfor("Actuary", "Pune")
time.sleep(0)


print("Job Details for Actuary")
print()
print("Details are in the following sequence:")
print("Job Position ")
print("Company Name ")
print("Location of Job ")
print()

jp1 = driver.find_element(By.XPATH, '//a[@class="disabled ember-view job-card-container__link job-card-list__title"]')
print( jp1.text)


jc1 = driver.find_element(By.XPATH, '//a[@class="job-card-container__link job-card-container__company-name ember-view"]')
print( jc1.text)

try:
    jl1= driver.find_element(By.XPATH, '//a[@class="job-card-container__metadata-item"]')
    print(jl1.text)
except:
    pass

#------------------------------------------------------------------------------------
print()

jp2 = driver.find_element(By.XPATH, '//a[@class ="disabled ember-view job-card-container__link job-card-list__title"]')
print(jp2.text)

jc2 = driver.find_element(By.XPATH, '//a[@class ="artdeco-entity-lockup__subtitle ember-view"]')
print(jc2.text)

try:
    jl2= driver.find_element(By.XPATH, '//a[@class="job - card - container__metadata - item"]')
    print(jl2.text)
except:
    pass
#------------------------------------------------------------------------------------
print()

# jp3 = driver.find_element(By.XPATH, '//*[@id="ember443"]')
# print(jp3.text)
#
# jc3 = driver.find_element(By.XPATH, '//*[@id="ember445"]')
# print(jc3.text)
#
# try:
#     jl3= driver.find_element(By.XPATH, '//*[@id="ember446"]/ul/li[1]')
#     print(jl3.text)
# except:
#     pass
# #------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------
# time.sleep(3)
#
# searchfor("School Teacher", "Pune")
# time.sleep(3)
# print("--------------------------------------------------------------------------")
# print("Job Details for School Teacher")
# print()
#
# jp4 = driver.find_element(By.XPATH, '//*[@id="ember1935"]')
# print("Job Position  -  " + jp4.text)
#
# jc4 = driver.find_element(By.XPATH, '//*[@id="ember1937"]')
# print("Company Name  -  " + jc4.text)
#
# try:
#     jl4= driver.find_element(By.XPATH, '//*[@id="ember1938"]/ul/li[1]')
#     print("Location of Job  -  " +jl4.text)
# except:
#     pass
# #------------------------------------------------------------------------------------
# print()
#
# jp5 = driver.find_element(By.XPATH, '//*[@id="ember1949"]')
# print("Job Position  -  " + jp5.text)
#
# jc5 = driver.find_element(By.XPATH, '//*[@id="ember1951"]')
# print("Company Name  -  " + jc5.text)
#
# try:
#     jl5= driver.find_element(By.XPATH, '//*[@id="ember1952"]/ul/li[1]')
#     print("Location of Job  -  " +jl5.text)
# except:
#     pass
# #------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------
# searchfor("Automobile Engineer", "Pune")
# print("--------------------------------------------------------------------------")
# print("Job Details for Automobile Engineer")
# print()
#
# jp6 = driver.find_element(By.XPATH, '//*[@id="ember2218"]')
# print("Job Position  -  " + jp6.text)
#
# jc6 = driver.find_element(By.XPATH, '//*[@id="ember2220"]')
# print("Company Name  -  " + jc6.text)
#
# try:
#     jl6= driver.find_element(By.XPATH, '//*[@id="ember2221"]/ul/li[1]')
#     print("Location of Job  -  " +jl6.text)
# except:
#     pass
# #------------------------------------------------------------------------------------
# print()
#
# jp7 = driver.find_element(By.XPATH, '//*[@id="ember2231"]')
# print("Job Position  -  " + jp7.text)
#
# jc7 = driver.find_element(By.XPATH, '//*[@id="ember2233"]')
# print("Company Name  -  " + jc7.text)
#
# try:
#     jl7= driver.find_element(By.XPATH, '//*[@id="ember2234"]/ul/li')
#     print("Location of Job  -  " + jl7.text)
# except:
#     pass


