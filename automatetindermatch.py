####Lets try this challenge.
from selenium import webdriver
browser = webdriver.Chrome()
# here we are starting the browser
##proceed to entering the tinder link so that the browser opens the link.
browser.get('https://www.tinder.com/')

##Getting Elements.
signupbtn = browser.find_element_by_css_selector('#content > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div > div.D\(f\).Fld\(c\).W\(100\%\).H\(100\%\).Ai\(c\) > div.Pos\(r\).D\(f\).W\(100\%\).Fld\(c\).Jc\(c\).Fxg\(1\).CenterAlign > button > span')
signupbtn.text
signupbtn.click()
