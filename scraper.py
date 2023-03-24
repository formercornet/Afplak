from pprint import pprint
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import MoveTargetOutOfBoundsException
import time
import re
import csv
import requests
def get_websites():

    with open("pages_num.txt", "r") as file:
        num = file.read()
        num = int(num) + 1
    # Define the URL pattern and range of pages to scrape
    url_pattern = "https://myip.ms/browse/sites/{page_num}/own/376714/cntVisitors/200/cntVisitorsii/1000"
    start_page = num 
    end_page = num + 25
    
    with open('websites_now.txt', 'w', encoding='utf-8') as file:
                file.write('')
    # Define a list of user agents to use for rotating requests

    print("program starting")

    # Start a new instance of Chrome with Selenium
    driver = webdriver.Chrome()  
    # Click in the middle of the screen to trigger the human verification
    width, height = driver.execute_script("return [window.innerWidth, window.innerHeight];")
    action = ActionChains(driver)
    action.move_by_offset(width/2, height*0.39).click().perform()

    # Loop over the pages and scrape the data
    for page_num in range(start_page, end_page+1):
        # Construct the URL for the current page
        url = url_pattern.format(page_num=page_num)
 
        driver.get(url)
        # Wait for the human verification to be completed
    
        # Parse the HTML content and extract the website names
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        td_tags = soup.find_all('td', {'class': 'row_name'})
        for td in td_tags:
            a_tag = td.find('a')
            website_name = a_tag.get_text()
            print(website_name)
            with open('websites.txt', 'a', encoding='utf-8') as file:
                file.write("{0}\n".format(website_name))
            with open('websites_now.txt', 'a', encoding='utf-8') as file:
                file.write("{0}\n".format(website_name))
        
        # Wait for 10 seconds before continuing to the next page
        print("Page {0} done!".format(page_num))
        time.sleep(10) # replace with an appropriate duration based on the human verification requirements
    file.close()
    # Close the browser when finished
    with open("pages_num.txt", "w") as file:
        file.write(str(end_page)) 

    driver.quit()

def email_scrape():

   
    hyper_text_string = "https://"
    websites_file = "websites_now.txt"
    output_file = "leads.csv"

    # open the websites file and read each line
    with open(websites_file) as f:
        websites = [line.strip() for line in f]

    num_websites = len(websites)
    c = 0
    # open the output file and write the header row
    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Website", "Company Name", "Email", "Facebook", "Twitter", "LinkedIn", "Instagram","Name"])
    # loop through each website and extract the requested information
    for website in websites:
        try:
            response = requests.get(hyper_text_string + website)
            soup = BeautifulSoup(response.content, "html.parser")
        
            # extract the company name from the website, if available
            company_name = soup.find("title").text.strip()
        
            # search for email addresses in the HTML content of the website
            email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(?!jpg|png|io)[A-Za-z]{2,}\b"
            emails = set(re.findall(email_regex, str(soup)))
            if emails == set():
                continue           
            # search for phone numbers in the HTML content of the website
            phone_regex = r"\+?\d{0,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
            phones = set(re.findall(phone_regex, str(soup)))
        
            # search for social media links in the HTML content of the website
            social_media = {"Facebook": "", "Twitter": "", "LinkedIn": "", "Instagram": ""}
            for a in soup.find_all("a", href=True):
                href = a["href"]
                if re.search(r"facebook\.com\/(?P<handle>[A-Za-z0-9.]+)", href):
                    social_media["Facebook"] = re.search(r"facebook\.com\/(?P<handle>[A-Za-z0-9.]+)", href).group("handle")
                elif re.search(r"twitter\.com\/(?P<handle>[A-Za-z0-9_]+)", href):
                    social_media["Twitter"] = re.search(r"twitter\.com\/(?P<handle>[A-Za-z0-9_]+)", href).group("handle")
                elif re.search(r"instagram\.com\/(?P<handle>[A-Za-z0-9._]+)", href):
                    social_media["Instagram"] = re.search(r"instagram\.com\/(?P<handle>[A-Za-z0-9._]+)", href).group("handle")
                elif re.search(r"linkedin\.com\/company\/(?P<handle>[A-Za-z0-9-]+)", href):
                    social_media["LinkedIn"] = re.search(r"linkedin\.com\/company\/(?P<handle>[A-Za-z0-9-]+)", href).group("handle")

            print("{0}/{1} done".format(c, num_websites))
            c += 1
            name = website.split(".")[0]
            # write the extracted information to the output file
            with open(output_file, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([website, company_name, ", ".join(emails), social_media["Facebook"], social_media["Twitter"], social_media["LinkedIn"], social_media["Instagram"],name])
                
        except:
            # print an error message if the website cannot be accessed or parsed
            print(f"Error processing {website}")
            num_websites -= 1

welcome = """Afplak
-----------------------------------------
Hey welcome to the best program ever made!
-----------------------------------------
Press '1' for website scraper
Press '2' for email scraper
-----------------------------------------"""
y = "x"

while y!="y":
    print(welcome)
    x = input()
    if x == "1":
        print("You selected 1 for website scraping, are you sure? (Y/N)")
        y = input().lower()
        if y == "y":
            get_websites()   
    elif x == "2":
        print("You selected 2 for email scraping, are you sure? (Y/N)")
        y = input().lower()
        if y == "y":
            email_scrape()

