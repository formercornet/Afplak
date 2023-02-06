import csv
import smtplib
import time
import email.utils
import uuid




# Your GoDaddy email address and password
sender_email = "marketing@afplak.com"
password = "GV$BZ&r2f%Ks"

# The CSV file containing recipient information
util_date = email.utils.formatdate(localtime=True)

csv_file = "recipients.csv"

# The file to store used emails
sent_file = "sent_emails.txt"

noads_line = "While visiting your Facebook page, I noticed that you do not run ads. Why's that? Based on your website & products, I bet you would smash it!"

ads_line = "While visiting your Facebook page, I noticed that you run ads. How are they performing? Based on your website & products, I bet you're smashing it!"

# Fixed email template
template = """Subject:[email_subject]

Dear [Name],

[Personalized_line1]

[Message1]

[Personalized_line2]

[Message2]

Best regards,

Ali
"""

# The rest of the message that follows [Personalized_line1]
message1 = "My name is Ali. I own Afplak.com - we're a marketing agency that specializes in e-commerce ads."
message2 = """From my initial look, I truly think that I can help you increase your profitability, looking at your products gave me some great ideas.

I would love to share them with you...are you available over the next few days to schedule a meeting?"""

#Connect to the GoDaddy SMTP server
server = smtplib.SMTP_SSL("smtpout.secureserver.net", 465)
server.ehlo()
server.login(sender_email, password)

# Read the list of used emails from the sent file
with open(sent_file, "r") as file:
    sent_emails = set(file.read().splitlines())

# Read recipient information from the CSV file
with open(csv_file, "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    recipients_noads = [row for row in reader if row[6] == "FALSE"] #DOES NOT RUN ADS
    file.seek(0)
    recipients_ads = [row for row in reader if row[6] == "TRUE"] # RUNS ADS

# Prompt the user to start sending emails
start = input("Enter 'yes' to start sending emails: ")
if start.lower() != "yes":
    print("Aborting.")
    server.quit()
    exit()

# Send an email to each recipient
for recipient in recipients_noads:
    email = recipient[1].strip()
    name = recipient[2].strip()
    email_subject = recipient[4].strip()
    personalized_line1 = recipient[5].strip()


    # Skip this recipient if their email has already been sent
    if email in sent_emails:
        continue

    # Fill in the recipient's name, personalized line 1, and the message in the email template
    email_body = template.replace("[Name]", name).replace("[Personalized_line1]", personalized_line1).replace("[Message1]", message1).replace("[Message2]", message2).replace("[Personalized_line2]", noads_line)

    # Send the email
    email_body = "From: {}\n".format(sender_email) + email_body
    email_body = "To: {}\n".format(email) + email_body
    email_body = "Date: {}\n".format(email.utils.formatdate(localtime=True)) + email_body
    email_body = "Message-ID: <{}@{}>\n".format(str(uuid.uuid1()), sender_email) + email_body
    email_body = "Content-Type: text/plain; charset=UTF-8\n" + email_body
    server.sendmail(sender_email, email, email_body)
    sent_emails.add(email)
    print(sender_email)
    print(email)
    print(email_body)
    # Add a delay of 120 seconds between each email sent
    time.sleep(60)

for recipient in recipients_ads:
    email = recipient[1].strip()
    name = recipient[2].strip()
    email_subject = recipient[4].strip()
    personalized_line1 = recipient[5].strip()

    # Skip this recipient if their email has already been sent
    if email in sent_emails:
        continue

    # Fill in the recipient's name, personalized line 1, and the message in the email template
    email_body = template.replace("[Name]", name).replace("[Personalized_line1]", personalized_line1).replace("[Message1]", message1).replace("[Message2]", message2).replace("[Personalized_line2]", ads_line).replace("email_subject", email_subject)

    # Send the email
    email_body = "From: {}\n".format(sender_email) + email_body
    email_body = "To: {}\n".format(email) + email_body
    email_body = "Date: {}\n".format(util_date) + email_body
    email_body = "Message-ID: <{}@{}>\n".format(str(uuid.uuid1()), sender_email) + email_body
    email_body = "Content-Type: text/plain; charset=UTF-8\n" + email_body
    server.sendmail(sender_email, email, email_body)
    sent_emails.add(email)
    print(sender_email)
    print(email)
    print(email_body)
    # Add a delay of 120 seconds between each email sent
    time.sleep(60)
# Save the list of used emails to the sent file
with open(sent_file, "w") as file:
    file.write("\n".join(sent_emails))



# Close the connection to the SMTP server
server.quit()