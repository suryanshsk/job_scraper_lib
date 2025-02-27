from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import os

class JobScraper:
    def __init__(self, website_url, update_interval=3600, output_file="jobs.json"):
        self.website_url = website_url
        self.update_interval = update_interval
        self.output_file = output_file
        self.jobs = []
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def fetch_jobs(self):
        """Fetches all job listings from the careers page."""
        try:
            self.driver.get(self.website_url)
            time.sleep(5)  # Wait for page to load
            
            job_elements = self.driver.find_elements(By.CSS_SELECTOR, 'div[jsname]')
            job_list = [job.text.strip() for job in job_elements if job.text.strip()]
            
            self.jobs = job_list
            return job_list

        except Exception as e:
            print(f"Error: {e}")
            return []

    def save_jobs(self):
        """Saves job listings to a JSON file."""
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
        with open(self.output_file, "w") as f:
            json.dump(self.jobs, f, indent=4)

    def auto_update(self):
        """Runs the scraper in a loop to update job listings periodically."""
        while True:
            print("Fetching jobs...")
            self.fetch_jobs()
            self.save_jobs()
            print(f"Jobs updated and saved to {self.output_file}")
            time.sleep(self.update_interval)

if __name__ == "__main__":
    scraper = JobScraper("https://www.google.com/about/careers/applications/jobs/results?has_remote=true")
    scraper.auto_update()
