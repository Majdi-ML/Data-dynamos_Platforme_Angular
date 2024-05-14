import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_linkedin_profiles(driver):
    profiles_data = []


    for page_number in range(1, 6):
       
        url = f"https://www.linkedin.com/search/results/people/?geoUrn=%5B%22102134353%22%5D&keywords=software%20engineer&origin=FACETED_SEARCH&searchId=2a17d78f-2ffa-4f96-bd7b-9012bc81869d&sid=S87si&page={page_number}"
        driver.get(url)

        # Attendre que les résultats de la recherche soient chargés
        WebDriverWait(driver, 240).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-result__info")))

        # Extraire les informations des profils sur la page actuelle
        profiles = driver.find_elements(By.CSS_SELECTOR, ".search-result__info")
        for profile in profiles:
            name = profile.find_element(By.CSS_SELECTOR, ".name.actor-name").text.strip()
            headline = profile.find_element(By.CSS_SELECTOR, ".subline-level-1").text.strip()
            location = profile.find_element(By.CSS_SELECTOR, ".subline-level-2").text.strip()
            current_company = profile.find_element(By.CSS_SELECTOR, ".search-result__truncate").text.strip()
            profiles_data.append({'Name': name, 'Headline': headline, 'Location': location, 'Current Company': current_company})

    return profiles_data

def save_to_csv(profiles_data):
    if not profiles_data:
        print("Aucun profil LinkedIn trouvé.")
        return

    filename = 'linkedin_profiles.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=profiles_data[0].keys())
        writer.writeheader()
        writer.writerows(profiles_data)
    print(f"Les données ont été enregistrées avec succès dans : {filename}")

def scrape_and_save_linkedin_profiles():
    # Set up Chrome driver
    service = Service("C:\\Users\\lando\\Downloads\\Compressed\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    # Navigate to LinkedIn login page
    driver.get("https://www.linkedin.com/login")

    # Wait for page to load and log in
    username = "majdimelliti22.g@gmail.com"  # Your email
    password = "Majdiamine12345"  # Your password

    username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "username")))
    username_field.send_keys(username)

    password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
    password_field.send_keys(password)

    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()

    # Wait for the dashboard page to load after login
    WebDriverWait(driver, 20).until(EC.url_contains("feed"))

    # Scrape LinkedIn profiles
    profiles_data = scrape_linkedin_profiles(driver)

    # Save the data to CSV
    save_to_csv(profiles_data)

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    scrape_and_save_linkedin_profiles()