#libraries 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import urllib.request, urllib.error, urllib.parse


# screenShot
def getscreenshotourl(url):
    #set the webdriver
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    #visit the webpage
    driver.get(url)
    time.sleep(5)
    #Set size
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment   
    #Tacke screenshot
    driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')
    
    time.sleep(5)
    driver.quit()
    
    
#webpage
def getwebshoot(url):
    #visit the web page
    response = urllib.request.urlopen(url)
    #read the content
    webContent = response.read()
    # create the html file
    f = open('web_page.html', 'wb')
    # write to the html file 
    f.write(webContent)
    f.close
    
# call funcations    
getscreenshotourl("https://www.cases.sheriahub.com/")
getwebshoot("https://www.cases.sheriahub.com/")