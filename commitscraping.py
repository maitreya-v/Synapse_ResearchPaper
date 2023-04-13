from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By

commit_list= []

url='https://github.com/facebook/react/commits/main'

driver = webdriver.Chrome()

# driver.get(url)

list_of_commits=[]
new_url=None
# older_btn_href=older_btn.__getattribute__('href')
total_commits=0
def get_commits(url):
    url=url
    driver.get(url)
    button = driver.find_elements(By.CLASS_NAME,'ellipsis-expander')

    for btn in button:
       btn.click()
    
    date = driver.find_elements(By.CLASS_NAME,'f5,text-normal')
    for d in date:
        print(d.text)
        
        
    commits = driver.find_elements(By.CLASS_NAME,'ws-pre-wrap')
    # print(commits[0].text)
    for commit in commits:

       list_of_commits.append(commit.text)
    older_btn = driver.find_elements(By.XPATH,'.//*[@id="repo-content-pjax-container"]/div/div[3]/div/a') 
    return older_btn[0].get_attribute('href')
    # older_btn_url=driver.find_elements(By.TAG_NAME,'   
new_url=get_commits('https://github.com/facebook/react/commits/main')    

# while(new_url!=None):
for i in range(1):
    new_url=get_commits(new_url)
    
# print(len(list_of_commits)) 
# print(list_of_commits)   

    
driver.close()    
