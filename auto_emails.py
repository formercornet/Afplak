import csv
import smtplib
import time
import email.utils
import uuid
import random
#MIME or BASE64 FRAMEWORK IMPORTED AND USED TO ADD SIGNATURE TO EMAILS INSTEAD OF USING NAMES or logo after the names

# Your GoDaddy email address and password
sender_email = "marketing@afplak.com"
password = "GV$BZ&r2f%Ks" #password removed for security reasons!!!

util_date = email.utils.formatdate(localtime=True)
# The CSV file containing recipient information
csv_file = "leads.csv"

# Fixed email template
template = """Subject:[name]?

Hey [name],

I know you get a bunch of emails like this so I don't wanna waste your time.

We'll do a 30 day trial period for free to generate sales. It's definitely worth a chat?

If you're interested, reply to this email and we'll schedule a meeting.

Thanks,

[sender]
Marketing Director

""" 


#sender = "0"
#correct = "0"
#while sender != "1" or sender != "2" or correct != "y":
#    sender_choose = """'1' if you're Ali 
#'2' if you're Seeno"""
#    print(sender_choose)
#    sender = input()
#    if sender == "1":
#        print("You're Ali correct?")
#        correct = input("Y/N: ").lower()
#        if correct == "y":
#            sender = "Ali Nazeer"
#            print("Welcome {0}!".format(sender))
#            break
#        elif correct == "n":
#           continue
#    elif sender == "2":
#        print("You're Seeno correct?")
#        correct = input("Y/N: ").lower()
#        if correct == "y":
#            sender = "Hussain Badreddeen"
#            print("Welcome {0}!".format(sender))
#            break
#        elif correct == "n":
#           continue

#Connect to the GoDaddy SMTP server
server = smtplib.SMTP_SSL("smtpout.secureserver.net", 465)
server.ehlo()
server.login(sender_email, password)

# Read the list of used emails from the sent file
with open("sent_emails.txt", "r") as file:
    sent_emails = set(file.read().splitlines())

all_names = []
all_emails = []
# Read recipient information from the CSV file
with open(csv_file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header row
    rows_to_keep = []
    for row in reader:
        if row[2].strip() != '':
            name_column = row[7]
            email_column = row[2]  # third column
            names = name_column.split(",")
            emails = email_column.split(',')
            all_emails.append(emails)
            all_names.append(names)
print("Numbers of emails to be sent:", len(all_emails))
print(all_names)
#print(all_names)




# Prompt the user to start sending emails
start = input("Enter 'yes' to start sending emails: ").lower()
if start.lower() != "yes":
    print("Aborting.")
    server.quit()
    exit()

counter = 0
for i in range(len(all_emails)):
    flag = False
    emails = all_emails[i]
    if len(emails) > 1:
        counter += 1
        print("Please select a email from the following: ")
        for j in range(len(emails)):
           print("{0} ({1}) \n".format((j+1), emails[j]))
           print("")
        email_selection = int(input())
        try:
           all_emails[i] = emails[(email_selection)-1]
        except:
           print("Error")

        print(all_emails[i])
print(counter)        
file = open("sent_emails.txt", "a")


sender_ali = "Ali Nazeer"
sender_seeno = "Hussain Badreddeen"
half = 0
c = 0
email_total = len(all_emails)
print(email_total)
ali_c = 0
seeno_c = 0
ali_seeno = ["Ali Nazeer", "Hussain Badreddeen"]
for i in range(len(all_emails)):

    email = all_emails[i][0]
    email.lstrip()
    name = all_names[i][0]
    email_subject = name
    half += 1
    sender_ = random.randint(0,1)
    if ali_seeno[sender_] == "Ali Nazeer":
        ali_c += 1
    if ali_seeno[sender_] == "Hussain Badreddeen":
        seeno_c += 1
       
    # Skip this recipient if their email has already been sent
    #if email in sent_emails:
    #   continue

    # Fill in the recipient's name, personalized line 1, and the message in the email template
    #if half < ((len(all_emails)) / 2):

    email_body = template.replace("[name]", name).replace("[email_subject]", email_subject).replace("[sender]", ali_seeno[sender_])
    #else:
    #    email_body = template.replace("[name]", name).replace("[email_subject]", email_subject).replace("[sender]", sender_seeno)
        
    
    # Send the email
    email_body = "From: {}\n".format(sender_email) + email_body
    email_body = "To: {}\n".format(email) + email_body
    email_body = "Date: {}\n".format(util_date) + email_body
    email_body = "Message-ID: <{}@{}>\n".format(str(uuid.uuid1()), sender_email) + email_body
    email_body = "Content-Type: text/plain; charset=UTF-8\n" + email_body
    try:
       server.sendmail(sender_email, email, email_body.encode('utf-8')) #all the above part is for complying withRFC 5322 Guidelines
       c += 1
        
    except:
       print("error, failed sending for {0}".format(email))
       email_total -= 1 
    
    sent_emails.add(email)
    print(email_body)
    print("{0}/{1} done".format(c, email_total))
    
    # Add a delay of 30 seconds between each email sent
    time.sleep(7)
    # Save the list of used emails to the sent file
    file.write("{0}\n".format(email))
print("Ali: ",ali_c)
print("Hussain: ",seeno_c)


        

