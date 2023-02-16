#!/usr/bin/env python3

import os
from datetime import date
import reports
import emails

"""
This script reads through text files to extract info (name and weight) of each fruit and generates a pdf report 
then generates and sends an email with the report as the attachment
"""

# assign directory
directory = 'supplier-data/descriptions'

# generate today's date
today = date.today()

# initialize empty list
fruit = []
 
# iterate over files in the directory
for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
        
    # separate filename from extension
    ff, e = os.path.splitext(filename)
    
    # ignore files that are not .txt
    if e != '.txt':
        continue
    
    # opens each text file and adds the info in the first two lines to the list 'fruit' with line breaks
    with open(file) as f:
        lines = f.readlines()
        fruit.append("name: " + lines[0] + "<br />")
        fruit.append("weight: " + lines[1] + "<br /> <br />") # double line breaks to add an empty line between each fruit entry
        

if __name__ == "__main__":
    
    # generate report with the following parameters
    report_path = "/tmp/processed.pdf"
    report_title = "Processed Update on " + str(today)
    report_body = "".join(fruit)
    
    reports.generate_report(report_path, report_title, report_body)
    
    # generate and send an email with the following parameters
    sender = "automation@example.com"
    recipient = "username@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment = report_path
    
    message = emails.generate_email(sender, recipient, subject, body, attachment)
    
    emails.send_email(message)
        
        