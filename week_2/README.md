## Week 2 - Working with Automated Tasks

- Working with the datetime Module
- Sending Emails with Python using SMTP via Gmail
- Automated Birthday Wisher Project Challenge
- Solution & Walkthrough for the Automated Birthday Wishes
- **Assignment 1:** Send Motivational Quotes on Mondays via Email

### Working with the datetime Module in Python

#### Introduction to datetime Module

- Overview of the datetime module
- Importing the datetime module

```python
import datetime
```

#### Understanding the Date and time Object

```python
from datetime import date

# Create a date object
today = date.today()
print("Today's date:", today)

# Access date attributes
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)
```

---

```python

from datetime import time

# Create a time object
current_time = time(14, 30, 45)
print("Current time:", current_time)

# Access time attributes
print("Hour:", current_time.hour)
print("Minute:", current_time.minute)
print("Second:", current_time.second)
print("Microsecond:", current_time.microsecond)

```

---

```python
from datetime import datetime

# Create a datetime object
now = datetime.now()
print("Current datetime:", now)

# Access datetime attributes
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)
print("Microsecond:", now.microsecond)
```

---

```python
# Create a datetime object

from datetime import datetime

# Create a datetime object
now = datetime.now()

# Format datetime using strftime
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted datetime:", formatted_date)

# Common format codes
# %Y - Year with century
# %m - Month as a zero-padded decimal number
# %d - Day of the month as a zero-padded decimal number
# %H - Hour (24-hour clock) as a zero-padded decimal number
# %M - Minute as a zero-padded decimal number
# %S - Second as a zero-padded decimal number
```

---

```python
# Parse a string into a datetime object
from datetime import datetime

# Parse a string into a datetime object
date_string = "2024-06-27 14:30:45"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed datetime:", parsed_date)
```

---

```python
# Calculate the difference between two dates

from datetime import datetime, timedelta

# Create a datetime object
now = datetime.now()

# Create a timedelta object
one_week = timedelta(weeks=1)

# Add one week to the current date
next_week = now + one_week
print("Date one week from now:", next_week)

# Subtract one week from the current date
last_week = now - one_week
print("Date one week ago:", last_week)
```

#### Working with Time Zones

- Using `pytz` library for time zone handling
- Converting datetime objects to different time zones

```python
from datetime import datetime
import pytz

# Create a datetime object
now = datetime.now()

# Define a timezone
utc = pytz.utc
eastern = pytz.timezone('US/Eastern')

# Localize the datetime object to UTC
now_utc = utc.localize(now)
print("Current datetime in UTC:", now_utc)

# Convert the datetime object to Eastern Time
now_eastern = now_utc.astimezone(eastern)
print("Current datetime in Eastern Time:", now_eastern)
```

#### Practical Examples

- Calculating the number of days between two dates
- Scheduling events with specific intervals
- Creating countdown timers

```python
from datetime import datetime, timedelta

# Calculate the number of days between two dates
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
delta = end_date - start_date
print("Number of days between dates:", delta.days)

# Schedule an event 10 days from now
now = datetime.now()
event_date = now + timedelta(days=10)
print("Event date:", event_date)

# Create a countdown timer
future_date = datetime(2024, 12, 31, 23, 59, 59)
remaining_time = future_date - now
print("Time remaining until New Year:", remaining_time)
```

#### Question 1: Calculate Age

Write a function `calculate_age` that takes a date of birth as a string in the format YYYY-MM-DD and returns the age of the person.

```python
from datetime import datetime

def calculate_age(dob: str) -> int:
    birth_date = datetime.strptime(dob, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day)
                                          < (birth_date.month, birth_date.day))
    return age
```

#### Question 2: Days Until Next Birthday

Write a function `days_until_next_birthday` that takes a date of birth as a string in the format YYYY-MM-DD and returns the number of days until the person's next birthday.

```python
from datetime import datetime, timedelta

def days_until_next_birthday(dob: str) -> int:
    birth_date = datetime.strptime(dob, "%Y-%m-%d")
    today = datetime.today()
    next_birthday = datetime(today.year, birth_date.month, birth_date.day)
    if next_birthday < today:
        next_birthday = datetime(today.year + 1, birth_date.month, birth_date.day)
    days_until_birthday = (next_birthday - today).days
    return days_until_birthday

# Example Test Cases
print(days_until_next_birthday("1990-06-15"))  # Output: (number of days until June 15, 2024)
print(days_until_next_birthday("2000-01-01"))  # Output: (number of days until January 1, 2025)
```

#### Class Practice Question - Find the Day of the Week

Write a function `find_day_of_week` that takes a date string in the format `YYYY-MM-DD` and returns the day of the week for that date.

```python
def find_day_of_week(date_str: str) -> str:
    pass

# Example Test Cases
# Input: "2024-06-27"
# Output: "Thursday"

# Input: "2024-01-01"
# Output: "Monday"

```

### Sending Emails with Python using SMTP - Using Mail Gun API

#### Pre Requisite

- **HTTP**: HTTP is a way for your web browser to ask for and get web pages, like when you go to `http://example.com`.

- **HTTPS**: HTTPS is a safer version of HTTP that protects your data, like when you visit a secure website at `https://example.com`.

- **SMTP**: SMTP is a way for computers to send emails to each other, like sending an email from `alice@example.com` to `bob@example.com`.

- **Domain Name**: A domain name is the easy-to-remember address of a website, like `example.com`, instead of a bunch of numbers.

- **IP**: An IP address is a unique number that identifies a computer on the internet, like `192.168.1.1` for your home Wi-Fi.

- **DNS**: DNS is like the phone book of the internet, translating domain names like `example.com` into IP addresses like `41.21.222.12`

- **MX Record**: An MX record is a type of DNS record that tells email servers where to send emails for a domain, like `mail.example.com`.

- **Mail Server**: A mail server is a computer that sends and receives emails, like `mail.example.com`.

- **Mail Client**: A mail client is a program that sends and receives emails, like Outlook, Thunderbird, or Gmail.

- **SMTP Server**: An SMTP server is a mail server that sends emails, like `smtp.example.com`.

- **SMTP Port**: An SMTP port is a number that identifies an SMTP server, like `25` for unencrypted email or `465` for encrypted email.

#### PORTS

- **HTTP**: Port 80 - Used for normal web traffic.
- **HTTPS**: Port 443 - Used for secure web traffic.
- **SMTP**: Port 25 - Used for sending emails.
- **POP3**: Port 110 - Used for receiving emails (Post Office Protocol).
- **IMAP**: Port 143 - Used for receiving emails (Internet Message Access Protocol).
- **FTP**: Port 21 - Used for transferring files.
- **SSH**: Port 22 - Used for secure remote access to computers.
- **DNS**: Port 53 - Used for domain name resolution.
- **Telnet**: Port 23 - Used for remote communication with devices.
- **SMTP over SSL/TLS**: Port 465 - Used for sending emails securely.
- **IMAP over SSL/TLS**: Port 993 - Used for securely receiving emails via IMAP.
- **POP3 over SSL/TLS**: Port 995 - Used for securely receiving emails via POP3.

#### Sending Emails with Python using SMTP and Gmail

- **SMTP**: Simple Mail Transfer Protocol (SMTP) is a protocol used to send emails between servers.

### Setting up Gmail for SMTP

- There are many programmatic email services, such as SendGrid, Mandrill, and Mailgun. These are useful if we’re generating a lot of email. They have official APIs and paid plans, and if we’re setting up a large-scale operation, it’s certainly worth looking into signing up to one of these services and using their Python libraries to send email. But for something small or personal, this can seem like a lot of effort, and there’s an alternative if we have a Gmail account (as many people do).

There’s an official Google Gmail Python API and module, but it’s quite annoying to set up and use. Python comes with the `smtplib` and `email` modules as part of the built-in library, and these are perfectly capable of sending email via Gmail after a little setup. We can even use them to send email from ourself to ourself. We can’t send too many emails this way, though. If we want to send tens or hundreds of emails to many different recipients, it’s best to investigate the programmatic email services mentioned above.

To use our Gmail account to send email this way, we first have to set up an app password for our Python script to use.
Go to the [App Password](https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmyaccount.google.com%2Fapppasswords&followup=https%3A%2F%2Fmyaccount.google.com%2Fapppasswords&ifkv=ASKXGp0mvda2mUS-4Iuq-oDCKDcqVEnbEjmFCNtztqKCJEOzwiC8zJQC6L1UTsauBa8d1T2HFUBu5A&osid=1&passive=1209600&rart=ANgoxcctWpClpk-e1e82lr36OXRpFS3yNTPoIQeGw7Gx1E_m8sTNMKNtUfkrYmm0REjRyYB_NygDdRaj6jyfNM_F_IDCclLfdg&service=accountsettings&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-32962069%3A1706579171935790&theme=glif) of your Google account.

Create App password and fill in a name (such as “My Python Script”). We’ll be shown a screen that lists our new app password.

_Make a note of this password somewhere_.

<img src="https://uploads.sitepoint.com/wp-content/uploads/2023/07/1689612633Example_2_gmail_app_password.png">

### Sending Emails with Python using SMTP

```python

import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("<YOUR_EMAIL>", "<YOUR_PASSWORD>")

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail("<SENDER_EMAIL>", "<RECEIPT_EMAIL>", message)

# terminating the session
s.quit()
```

### Automated Birthday Wisher Project Challenge

Creating an Automated Birthday Wisher project in Python using SMTP and Gmail involves the following steps:

1. Set Up Gmail SMTP Access: Allow less secure apps or create an app-specific password if you have two-factor authentication enabled.

2. Prepare a List of Birthdays: Store your contacts' birthdays in a CSV file.

3. Write a Python Script: Use the smtplib library to send emails and the pandas library to read the CSV file.

#### Step 1: Set Up Gmail SMTP Access

Follow the above way to set up Gmail SMTP access.

#### Step 2: Prepare a List of Birthdays

```csv
name,email,month,day
Alice,alice@example.com,7,6
Bob,bob@example.com,8,15
```

#### Step 3: Write a Python Script

```python

import smtplib
import pandas as pd
from datetime import datetime

# SMTP email server details
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
GMAIL_USER = "your-email@gmail.com"
GMAIL_PASSWORD = "your-email-password"

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
```

#### Schedule the Script to Run Daily

_Scheduling the Script_

##### For Windows Task Scheduler:

- Open Task Scheduler.
- Create a new task.
- Set the trigger to daily.
- Set the action to run python path\to\birthday_wisher.py.

##### For Unix-like Systems (using cron):

- Open the crontab file: crontab -e.
- Add a new line: 0 9 \* \* \* /usr/bin/python3 /path/to/birthday_wisher.py (This will run the script every day at 9 AM).
