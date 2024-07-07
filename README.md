# LinkedIn Job Scraper and Profile Extractor

## Overview

This project provides a Python script to scrape job postings from LinkedIn and extract profile information. It uses the Selenium and BeautifulSoup libraries for scraping and data extraction, and sends an email with the results in an Excel file.

## Features

- **Job Scraping:** Fetches job listings based on specific keywords from LinkedIn job search URLs.
- **Profile Scraping:** Extracts profile information from a LinkedIn profile URL, including name, title, location, and LinkedIn profile URL.
- **Email Notification:** Sends an email with the top 3 job postings and profile information attached as an Excel file.

## Requirements

- Python 3.x
- Selenium
- BeautifulSoup
- Pandas
- `webdriver-manager`
- `requests`
- `smtplib` (standard library)
- `email` (standard library)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   
2. **Navigate to the project directory:**
    ```bash
   cd yourrepository

3. **Install the required packages:**
   ```bash  
   pip install selenium beautifulsoup4 pandas webdriver-manager requests

## Configuration

**Update the Email Credentials**

1. **Edit the script to include your email credentials in the send_email function:**


```python 
sender_email = "your_email@gmail.com" 
sender_password = "your_email_password"
recipient_emails = ["recipient@example.com"]  


