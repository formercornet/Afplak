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
        # convert to lowercase and strip leading/trailing whitespace
        email = email.lower().strip()
        # remove "<" and ">" characters from email address if present
        if email.startswith("<") and email.endswith(">"):
            email = email[1:-1]
        if email not in seen_emails and not any(banned_substring in email for banned_substring in banned_substrings) and email not in blacklist:
            cleaned_emails.append(email)
            seen_emails.add(email)
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
