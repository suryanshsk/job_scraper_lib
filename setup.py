from setuptools import setup, find_packages

setup(
    name="job_scraper_lib",
    version="0.2.1",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "webdriver_manager"
    ],
    entry_points={
        "console_scripts": [
            "job_scraper=job_scraper_lib.scraper:JobScraper"
        ],
    },
    author="Avanish Singh",
    author_email="suryanshskcontact@gmail.com",
    description="A Python library for scraping job listings from company career pages",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/suryanshsk/job_scraper_lib",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
