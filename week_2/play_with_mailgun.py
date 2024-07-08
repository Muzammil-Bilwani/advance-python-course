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
