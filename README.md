# Automated Email Sender with Python and Pandas

This Python script allows you to send custom emails to multiple companies listed in an Excel file, along with attaching your resume. It uses the Pandas library to read company details from the Excel file and the smtplib library to send emails through your email provider. Make sure you have the required libraries installed before running the script.

## Prerequisites

- Python 3.x
- Pandas library (`pip install pandas`)
- smtplib library (pre-installed with Python)
- email library (pre-installed with Python)

## How to Use

1. Save the list of companies and their respective email addresses in an Excel file named `companies.xlsx`. The Excel file should have two columns: `Company` and `Email`.
2. Replace the variables `sender_email` and `sender_password` with your email credentials.
3. Customize the email template in the `message_template` variable to fit your needs. You can use placeholders like `{company_name}` that will be replaced with the actual company name while sending emails.
4. Replace `resume.pdf` with the path to your actual resume file in the variable `resume_file`.

## Email Content

The email template provided in the script is a sample message that can be customized according to your requirements. Feel free to modify it to create a more personalized and engaging email.

## Important Note

- **Use this script responsibly:** Sending bulk emails may be subject to anti-spam regulations, so ensure that you have the necessary permissions to send emails to the recipients.
- **Gmail Configuration:** If you are using a Gmail account, make sure to allow "Less Secure Apps" or generate an "App Password" to use as the sender_password. For other email providers, follow their respective authentication methods.

## Running the Script

Simply execute the Python script, and it will automatically send personalized emails to each company in the Excel file, along with attaching your resume.

```python
python email_sender.py
```
make sure the paths for the resume and the Excel are defined correctly

## Disclaimer
The authors assume no responsibility for any misuse of this script. Use it responsibly and only for legitimate purposes.
