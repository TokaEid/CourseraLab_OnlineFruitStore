#!/usr/bin/env python3

import os.path
import email.message
import mimetypes
import smtplib

def generate_email(sender, recipient, subject, body, attachment_path):
    """ Generates an email with the desired sender, recipient, subject, body and possibility of attachment file """
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)
    
    # generates an email without an attachment
    if not attachment_path:
        return message
    
    else: 
        # in case attachment exists:
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)
        
        with open(attachment_path, 'rb') as ap:
            message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=attachment_filename)
            
        return message
    
    
def send_email(message):
    """ Sends the generated email through an SMTP server """
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
    