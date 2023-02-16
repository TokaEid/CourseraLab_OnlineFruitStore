#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(file_path, title, body):
    """ Generates a report as a pdf file with the input 'title' and 'body' """
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(file_path)
    report_title = Paragraph(title, styles["h1"])
    report_body = Paragraph(body, styles["BodyText"])
    empty_line = Spacer(1,20)
    
    report.build([report_title, empty_line, report_body])