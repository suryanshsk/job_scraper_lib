# Job Scraper Library

## Overview
This Python library allows users to **automatically extract job listings** from a company's career page. The library scrapes job postings and updates the data **automatically** to ensure real-time job availability.

## Features
- Extracts job listings from any career page URL
- Automatically updates job data
- Easy to integrate into job board websites
- Uses **Selenium** and **WebDriver-Manager** for automation

## Installation
Before using the library, install the required dependencies:

```bash
pip install selenium webdriver-manager
```

## Usage
Here is how to use the library to scrape job postings:

```python
from job_scraper import JobScraper

# Initialize scraper with career page URL
scraper = JobScraper("https://www.google.com/about/careers/applications/jobs/results?has_remote=true")

# Get job listings
jobs = scraper.fetch_jobs()

# Print job details
for job in jobs:
    print(job)
```

## Requirements
- Python 3.7+
- Google Chrome (Latest Version)
- ChromeDriver (Managed automatically by `webdriver-manager`)

## Troubleshooting
### "ImportError: No module named 'selenium'"
Run:
```bash
pip install selenium webdriver-manager
```

### "ChromeDriver Version Error"
If ChromeDriver version is outdated, update it:
```bash
pip install --upgrade webdriver-manager
```

## Contributing
Feel free to submit **pull requests** for improvements or bug fixes.

## License
This project is **open-source** under the MIT License.

