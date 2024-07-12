
import smtplib
import pandas as pd
from datetime import datetime

# SMTP email server details
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
GMAIL_USER = "<YOUR_EMAIL>"
GMAIL_PASSWORD = "<YOUR_PASSWORD>"

def send_email(to_address, subject, message):
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            email_message = f"Subject: {subject}\n\n{message}"
            server.sendmail(GMAIL_USER, to_address, email_message)
        print(f"Successfully sent email to {to_address}")
    except Exception as e:
        print(f"Failed to send email to {to_address}: {e}")

def check_and_send_wishes():
    today = datetime.today()
    month = today.month
    day = today.day

    # Read the birthday CSV file
    birthdays = pd.read_csv("birthdays.csv")

    for index, row in birthdays.iterrows():
        if row["month"] == month and row["day"] == day:
            name = row["name"]
            email = row["email"]
            subject = "Happy Birthday!"
            message = f"Dear {name},\n\nWishing you a very Happy Birthday!\n\nBest Regards,\nYour Friend"
            send_email(email, subject, message)

if __name__ == "__main__":
    check_and_send_wishes()