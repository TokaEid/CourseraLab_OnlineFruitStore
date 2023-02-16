#!/usr/bin/env python3

import os
import shutil
import psutil
import socket
import emails

"""
This script calls on functions that check various aspects of the computer and disk usage and properties 
and sends an email alert for any checks that fail
"""


def cpu_usage(time):
    """
    Returns true if cpu usage is less than or equal to 80%
    """
    check = psutil.cpu_percent(time) <= 80
    return check

def disk_usage(disk):
    """
    Returns true if free space on disk is greater than or equal to 20% of total space
    """
    usage = shutil.disk_usage(disk)
    check = (usage.free / usage.total) * 100 >= 20
    return check

def available_memory():
    """
    Returns true if available memory is greater than or equal to 500 MB
    """
    usage = psutil.virtual_memory()
    check = (usage.available / 1e6) >= 500
    return check

def check_localhost():
    """
    Returns true if localhost can be resolved to 127.0.0.1
    """
    check = socket.gethostbyname('localhost') == '127.0.0.1'
    return check


if __name__ == "__main__":
    
    sender = "automation@example.com"
    recipient = "username@example.com"
    body = "Please check your system and resolve the issue as soon as possible."
    attachment = None
    
    if not cpu_usage(1):
        subject = "Error - CPU usage is over 80%"
        msg = emails.generate_email(sender, recipient, subject, body, attachment)
        emails.send_email(msg)
        
        
    if not disk_usage('/'):
        subject = "Error - Available disk space is less than 20%"
        msg = emails.generate_email(sender, recipient, subject, body, attachment)
        emails.send_email(msg)
        
    if not available_memory():
        subject = "Error - Available memory is less than 500MB"
        msg = emails.generate_email(sender, recipient, subject, body, attachment)
        emails.send_email(msg)
        
        
    if not check_localhost():
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
        msg = emails.generate_email(sender, recipient, subject, body, attachment)
        emails.send_email(msg)
        
        
    