from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import random



# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def get_first_result_link(question_num):
    try:
        # Construct direct search URL
        # query = f"https://search.brave.com/search?q=aws+saa+examtopics+question+{question_num}"
        query = f"https://www.google.com/search?q=exam+AWS+Certified+Cloud+Practitioner+topic+1+question+{question_num}"
        # https://search.brave.com/search?q=aws+saa+examtopics+question+241
        driver.get(query)
        
        # Wait for results
        first_result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div#search a"))
        )
        return first_result.get_attribute("href")
    except Exception as e:
        print(f"Error with question {question_num}: {str(e)}")
        return "No result found"

# Create list to store results
results = []

# Loop through questions 241 to 351
for question_num in range(241, 988):
    link = get_first_result_link(question_num)
    
    result = {
        "question_number": question_num,
        "link": link
    }
    results.append(result)
    
    print(f"Processed question {question_num}")
    
    # Random delay between 2-5 seconds to avoid detection
    time.sleep(random.uniform(2, 5))

# Save to JSON file
try:
    with open("aws_saa_questions.json", "w") as json_file:
        json.dump(results, json_file, indent=4)
    print("Scraping completed! Results saved to aws_saa_questions.json")
except Exception as e:
    print(f"Error saving JSON: {str(e)}")

# Close the browser
driver.quit()