import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Excel file path
excel_file = 'companies.xlsx' #replace, save the list of companies and their email as an xlsx file

# Email credentials
sender_email = '' #your email 
sender_password = ' ' # your password

# Read company details from Excel file
df = pd.read_excel(excel_file)
companies = df['Company'].tolist()
emails = df['Email'].tolist()

# Email content
message_template = '''
Dear Hiring Manager,

I hope this email finds you well. I am writing to express my interest in joining your company.. I came across {company_name} and was immediately drawn to the innovative work and opportunities for growth within your organization.

......
custom body
'''

# Iterate over companies and send emails
for company, email in zip(companies, emails):
    # Create email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = email
    message['Subject'] = f"Coustom subject"
    # Fill in the email body with company name
    message_body = message_template.format(company_name=company)
    message.attach(MIMEText(message_body, 'plain'))

    # Attach resume file
    resume_file = 'resume.pdf'  # Replace with your actual resume file path
    attachment = open(resume_file, 'rb')
    resume_part = MIMEBase('application', 'octet-stream')
    resume_part.set_payload(attachment.read())
    encoders.encode_base64(resume_part)
    resume_part.add_header('Content-Disposition', f'attachment; filename= {resume_file}')
    message.attach(resume_part)

    # Send email
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465) # configure as per your mail provider
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, message.as_string())
        server.quit()
        print(f"Email sent to {company} successfully!")
    except smtplib.SMTPException as e:
        print(f"Failed to send email to {company}. Error: {str(e)}")
