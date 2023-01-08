import smtplib

sender_address = senders_mail@gmail.com"
reciever_address = recievers_mail@gmail.com"
password = "password"
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)


s.starttls()

# Authentication
s.login(sender_address, password)
 

message = "This email has been sent by Anonymous from python"
 
# sending the mail
s.sendmail(sender_address, reciever_address, message)
 

s.quit()