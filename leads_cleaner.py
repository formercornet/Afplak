import csv
import os

# Read the banned substrings from a set file
banned_substrings = set()
with open('banned_substrings.txt', 'r') as f:
    for line in f:
        banned_substrings.add(line.strip())

# Read the email blacklist from a file
blacklist = set()
with open('blacklist.txt', 'r') as f:
    for line in f:
        blacklist.add(line.strip())

# Define a function to remove duplicates from a list of emails
def clean_emails(emails):
    cleaned_emails = []
    seen_emails = set()
    for email in emails:
        if email.lower().find("u003e") != -1:
                temp_email = email.lower().strip("u003")
                email = temp_email[1]
        if email.lower() not in seen_emails and not any(banned_substring in email.lower() for banned_substring in banned_substrings) and email.lower() not in blacklist and email.lower() not in cleaned_emails:
            cleaned_emails.append(email.lower())
            seen_emails.add(email.lower())
        
    return cleaned_emails

with open('leads.csv', 'r') as f, open('output.csv', 'w', newline='') as out_f:
    reader = csv.reader(f)
    writer = csv.writer(out_f)
    header = next(reader)
    writer.writerow(header) # write header to output file
    for row in reader:
        if row[2] == "":
            continue
        emails = row[2].split(",")
        cleaned_emails = clean_emails(emails)
        row[2] = ",".join(cleaned_emails)
        writer.writerow(row)
# remove original file
os.remove('leads.csv')

# rename output file to original file name
os.rename('output.csv', 'leads.csv')
