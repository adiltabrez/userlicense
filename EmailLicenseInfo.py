import smtplib

s = smtplib.SMTP('mail.google.com', 587)
s.starttls()
s.login("adil.tabrez@gmail.com", "Glaksyk!@#4567")
message = "This is a test email from Python."
s.sendmail("adil.tabrez@gmail.com","adil.tabrez@gmail.com",message)
s.quit()