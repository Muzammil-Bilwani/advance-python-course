## Week 2 - Working with Automated Tasks

- Working with the datetime Module
- Sending Emails with Python using SMTP via Mail gun
- Automated Birthday Wisher Project Challenge
- Solution & Walkthrough for the Automated Birthday Wishes
- **Challenge 1:** Send Motivational Quotes on Mondays via Email

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

- **SMTP (Simple Mail Transfer Protocol):** It is a protocol that allows you to send emails. It is used to send emails from one server to another.

- **SendGrid:** It is a cloud-based SMTP provider that allows you to send emails without having to maintain email servers.

- **Setting Up SendGrid Account:**
  1. Create a SendGrid account
  2. Generate an API key
  3. Verify your email address
