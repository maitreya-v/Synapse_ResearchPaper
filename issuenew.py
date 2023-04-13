from selenium import webdriver

from selenium.webdriver.common.by import By
import re
import pandas as pd

url='https://github.com/facebook/react/issues'
driver = webdriver.Chrome()
driver.get(url)
list_of_issues=[]
total_issues=0
new_url='https://github.com/facebook/react/issues'
def get_issues(url):
    global total_issues
    
    url = str(url)
    driver.get(url)
    issues = driver.find_elements(By.CLASS_NAME,'markdown-title')
    total_issues = total_issues+len(issues)
    for issue in issues:
        list_of_issues.append(issue.text)
    next_btn = driver.find_elements(By.CLASS_NAME,'next_page') 
    return next_btn[0].get_attribute('href')


while(new_url!=None):
# for i in range(1):
    new_url=get_issues(new_url)
        
    
# print(total_issues)
driver.close()

dataDf = pd.DataFrame()
# print(list_of_issues)
dataDf["issues"] = list_of_issues
print(dataDf)

# this will return a CSV file
dataDf.to_csv(r'react_issues.csv', index=False) 