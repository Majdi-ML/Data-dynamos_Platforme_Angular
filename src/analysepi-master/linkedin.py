import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def login_linkedin(driver, username, password):
    # Navigate to LinkedIn login page
    driver.get("https://www.linkedin.com/login")

    # Wait for page to load and log in
    username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "username")))
    username_field.send_keys(username)

    password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
    password_field.send_keys(password)

    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()

    # Wait for the dashboard page to load after login
    WebDriverWait(driver, 20).until(EC.url_contains("feed"))

def search_software_engineer_in_tunisia(driver):
    # Navigate to LinkedIn search page for "Software Engineer" in Tunisia
    driver.get("https://www.linkedin.com/search/results/people/?geoUrn=%5B%22102134353%22%5D&keywords=software%20engineer&origin=FACETED_SEARCH&searchId=2a17d78f-2ffa-4f96-bd7b-9012bc81869d&sid=S87si")

def scrape_linkedin_profiles(driver):
    # Initialize lists to store data
    linkedinProfileUrls = []
    fullNames = []
    firstNames = []
    lastNames = []
    linkedinHeadlines = []
    locations = []
    linkedinProfileSlugs = []
    ids = []
    createdAts = []
    updatedAts = []

    # Find all profile links on the page
    profile_links = driver.find_elements(By.XPATH, "//a[@class='app-aware-link']")
    profile_urls = [link.get_attribute('href') for link in profile_links]

    # Iterate through each profile URL
    for profile_url in profile_urls:
        # Visit profile page
        driver.get(profile_url)
        time.sleep(3)  # Wait for profile page to load (reduced time to 3 seconds)

        # Extract desired information
        try:
            linkedinProfileUrl = profile_url
            fullName = driver.find_element(By.XPATH, "//h1[contains(@class, 'text-heading-xlarge')]").text
            firstName = fullName.split()[0]
            lastName = fullName.split()[-1]
            linkedinHeadline = driver.find_element(By.XPATH, "//h2[contains(@class, 'mt1')]//span").text
            location = driver.find_element(By.XPATH, "//h3[contains(@class, 'mt1')]//span").text
            linkedinProfileSlug = profile_url.split("/")[-2]
            id = "" # Add logic to extract ID if available
            createdAt = "" # Add logic to extract createdAt if available
            updatedAt = "" # Add logic to extract updatedAt if available

            # Append data to lists
            linkedinProfileUrls.append(linkedinProfileUrl)
            fullNames.append(fullName)
            firstNames.append(firstName)
            lastNames.append(lastName)
            linkedinHeadlines.append(linkedinHeadline)
            locations.append(location)
            linkedinProfileSlugs.append(linkedinProfileSlug)
            ids.append(id)
            createdAts.append(createdAt)
            updatedAts.append(updatedAt)
        except Exception as e:
            print(f"Error processing profile: {profile_url}. Error: {e}")

    # Create a DataFrame from the extracted data
    data = {'linkedinProfileUrl': linkedinProfileUrls, 
            'fullName': fullNames, 
            'firstName': firstNames, 
            'lastName': lastNames, 
            'linkedinHeadline': linkedinHeadlines, 
            'location': locations, 
            'linkedinProfileSlug': linkedinProfileSlugs, 
            'id': ids, 
            'createdAt': createdAts, 
            'updatedAt': updatedAts}
    df = pd.DataFrame(data)

    # Write the DataFrame to an Excel file
    excel_file = 'linkedin_profiles.xlsx'
    df.to_excel(excel_file, index=False)

    print("Data has been successfully saved to:", excel_file)

if __name__ == "__main__":
    # Set up Chrome driver
    service = Service("C:\\Users\\lando\\Downloads\\Compressed\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    # Login to LinkedIn
    username = "majdimelliti22.g@gmail.com"  # Your email
    password = "Majdiamine12345"  # Your password
    login_linkedin(driver, username, password)

    # Search for software engineers in Tunisia
    search_software_engineer_in_tunisia(driver)

    # Scrape LinkedIn profiles
    scrape_linkedin_profiles(driver)

    # Close the browser
    driver.quit()
