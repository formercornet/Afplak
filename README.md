# 📧 Afplak Lead Generation Suite

A Python-based outreach automation toolkit built for a marketing agency. Scrapes leads, cleans data, and sends personalized cold emails at scale.

## Tools

### 🕷️ Website & Email Scraper
Scrapes websites from myip.ms, extracts emails, social media handles, and company names. Outputs structured CSV leads file.

### 📬 Email Outreach Automator  
Sends personalized cold emails via SMTP with dynamic templates based on whether a lead runs Facebook ads or not. RFC 5322 compliant. Tracks sent emails to avoid duplicates.

### 🧹 Lead Cleaner
Deduplicates and sanitizes email lists. Filters banned substrings and blacklisted addresses. Outputs clean leads CSV ready for outreach.

## Tech Stack
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=flat&logo=selenium&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4-orange?style=flat)

## Features
- 🔍 Automated lead scraping with pagination support
- 📊 Social media handle extraction (Facebook, Instagram, LinkedIn, Twitter)
- ✉️ Personalized email sequences based on lead behavior
- 🚫 Blacklist and duplicate filtering
- ⏱️ Rate limiting to avoid spam detection

## Note
Credentials and API keys removed for security purposes.
