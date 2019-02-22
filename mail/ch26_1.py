import smtplib

# 請注意封包名稱或命名的py名稱，不能是email.py.....
mySMTP = smtplib.SMTP("smtp.gmail.com", 587)
print(mySMTP.ehlo())
print(mySMTP.starttls())
print(mySMTP.login("pattycheng2008@gmail.com", "patty0128"))
status = mySMTP.sendmail("pattycheng2008@gmail.com","pattycheng2008@gmail.com",
                         "Subject: My first test\nMessage from python")
print(status)
mySMTP.quit()