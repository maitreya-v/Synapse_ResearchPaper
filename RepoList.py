from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

# Replace the following variables with the URL of the website
# and the path to the chromedriver executable on your machine
website_url = "https://hackernoon.com/githubs-top-100-most-valuable-repositories-out-of-96-million-bb48caa9eb0b"
chromedriver_path = "/path/to/chromedriver"

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
# Run Chrome in headless mode to avoid opening a browser window
chrome_options.add_argument("--headless")

# Create a new Chrome WebDriver instance
browser = webdriver.Chrome(
    executable_path=chromedriver_path, options=chrome_options)

# Navigate to the website
browser.get(website_url)

# Find elements on the page by XPath and extract data
# Example: Find an element by its XPath and get its text content

# //*[@id = "__next"]/div/main/div/div[6]/div/ol/li[2]/p[4]/a[1]
# //*[@id = "__next"]/div/main/div/div[6]/div/ol/li[3]/p[4]/a[1]
# //*[@id="__next"]/div/main/div/div[6]/div/ol/li[100]/p[4]/a[1]

# element = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div[6]/div/ol/li[1]/p[4]/a[1]')
# link = element.text
# print(link)

githubLinks = []
for i in range(1, 101):  # Adjust the range as needed
    # Construct the dynamic XPath expression with the loop variable
    xpath = f'//*[@id="__next"]/div/main/div/div[6]/div/ol/li[{i}]/p[4]/a[1]'
    # Find the element using the constructed XPath expression
    element = browser.find_element(By.XPATH, xpath)
    githubLink = element.text
    githubLinks.append(githubLink)
print(githubLinks)
print(type(githubLinks))

# Close the browser
browser.quit()

# Specify the file name for the CSV file
filename = 'githubRepoLinks.csv'

columns = ['Repo']

# Open the CSV file in write mode
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)

    # Write the column names as the first row
    csvwriter.writerow(columns)

    # Write each item in the list as a separate row
    for item in githubLinks:
        csvwriter.writerow([item])

print(f"CSV file '{filename}' has been created successfully!")







