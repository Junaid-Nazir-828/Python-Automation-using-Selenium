# This file covers:
# button click
# implicit wait
# explicit wait
import os  # importing for adding file to PATH
from selenium import webdriver
from selenium.webdriver.common.by import By  # will be used in explicit wait and finding elements
from selenium.webdriver.support.ui import WebDriverWait  # importing for explicit wait
from selenium.webdriver.support import expected_conditions as EC  # importing for explicit wait

# adding the main folder to PATH which is an environmental variable
os.environ['PATH'] += r";C:/SeleniumDriver"

# getting to target site
driver = webdriver.Chrome()
driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")

# implicit wait is used to wait before any action
# note that if we used implicit wait, it will be applied
# to every action after its use.
# In this case program will automatically wait
# for 5 sec before performing any action
driver.implicitly_wait(5)
myElement = driver.find_element(By.ID, 'downloadButton')
myElement.click()

# Let say there is a text 'downloaded!' that shows up
# after the download, and we want to print it. In this case
# if we write code without explicit wait, it will not be waiting for the desired text to show up.
# In these cases where we want some condition to be true and then perform certain action
# we use explicit wait

# code without explicit wait:
### complete_text = driver.find_element(By.CLASS_NAME, 'progress-label')
### print(f'Output : {complete_text.text}')

# code with explicit wait:
WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        # takes two arguments
        (By.CLASS_NAME, 'progress-label'),  # Element Filtration
        'Complete!'  # Expected Text
    )
)
# second attribute to WebDriverWait() is time in seconds, that the driver will wait until the condition
# written next to EC (Expected Condition) becomes true.

# close = driver.find_element(By.CLASS_NAME, 'ui-button ui-corner-all ui-widget')
# close.click()
