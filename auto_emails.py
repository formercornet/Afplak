import csv
import smtplib
import time
import email.utils
import uuid
#MIME or BASE64 FRAMEWORK IMPORTED AND USED TO ADD SIGNATURE TO EMAILS INSTEAD OF USING NAMES or logo after the names

# Your GoDaddy email address and password
sender_email = "marketing@afplak.com"
password = "" #password removed for security reasons!!!

util_date = email.utils.formatdate(localtime=True)
# The CSV file containing recipient information
csv_file = "leads.csv"

# Fixed email template
template = """Subject:[email_subject]

Dear [Name],

Hi {{first_name}},

I know you get a bunch of emails like this so I don't wanna waste your time.

We'll do a 30 day trial period for free to generate sales. You think it's worth a chat?

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
#server = smtplib.SMTP_SSL("smtpout.secureserver.net", 465)
#server.ehlo()
#server.login(sender_email, password)

# Read the list of used emails from the sent file
with open("sent_emails.txt", "r") as file:
    file = set(file.read().splitlines())


all_names = []
all_emails = []
# Read recipient information from the CSV file
with open(csv_file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header row
    rows_to_keep = []
    for row in reader:
        if row[2].strip() != '':  # check if the cell is not empty
            name_column = row[8]
            email_column = row[2]  # third column
            names = name_column.split(",")
            emails = email_column.split(',')
            all_emails.append(emails)
            all_names.append(names)
print("Numbers of emails to be sent:", len(all_emails))
#print(all_names)




# Prompt the user to start sending emails
#start = input("Enter 'yes' to start sending emails: ").lower()
#if start.lower() != "yes":
#    print("Aborting.")
#    server.quit()
#    exit()


for i in range(len(all_emails)):
    email = all_emails[i]
    if len(email) > 1:
        print("Please select a email from the following: ")
        for j in range(len(email)):
            print("{0} ({1}) \n".format((j+1), email[j]))
        email_selection = int(input())
        final_email = email[(email_selection)-1]
        print(final_email)
        





   # 
   # name = all_names[i]
   # email_subject = recipient[4].strip()
   # personalized_line1 = recipient[5].strip()


   ## Skip this recipient if their email has already been sent
   # if email in sent_emails:
   #     continue

   # # Fill in the recipient's name, personalized line 1, and the message in the email template
   # email_body = template.replace("[Name]", name).replace("[Personalized_line1]", personalized_line1).replace("[Message1]", message1).replace("[Message2]", message2).replace("[Personalized_line2]", noads_line).replace("[email_subject]", email_subject)
    
   # # Send the email
   # email_body = "From: {}\n".format(sender_email) + email_body
   # email_body = "To: {}\n".format(email) + email_body
   # email_body = "Date: {}\n".format(util_date) + email_body
   # email_body = "Message-ID: <{}@{}>\n".format(str(uuid.uuid1()), sender_email) + email_body
   # email_body = "Content-Type: text/plain; charset=UTF-8\n" + email_body
   # server.sendmail(sender_email, email, email_body.encode('utf-8')) #all the above part is for complying withRFC 5322 Guidelines
   # sent_emails.add(email)
   # print(sender_email)
   # print(email)
   # print(email_body)
   # # Add a delay of 30 seconds between each email sent
   # time.sleep(30)
   # # Save the list of used emails to the sent file
   # with open(sent_file, "w") as file: # added + indented to adjust file after each sent email instead of at the end of script
   #   file.write("\n".join(sent_emails))

        

