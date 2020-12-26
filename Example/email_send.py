import smtplib
#=========================================================
#sender email
sender_email = "ashutoshkumargautam00000@gmail.com"
#sender email password
sender_email_password = "ashutoshkumar@123"
#============================================
recevier = input("who want want send you")
msg = input(" what's the message")
#=========================================================
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(sender_email, sender_email_password)
message = msg
s.sendmail(sender_email, recevier, message)
s.quit()
print("Email sent successfully")
