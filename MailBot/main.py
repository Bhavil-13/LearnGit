import smtplib
from abc import msg

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('sender@gmail.com','password')
server.sendmail('sender@gmail.com', 'rcvr@gmail.com', msg.message)
