#Libraries
import string
import argparse
import smtplib
from email.mime.text import MIMEText
#Argument Parser 
parser = argparse.ArgumentParser()
#Argument
parser.add_argument("--libero", "-l", action="store_true", help="libero's smtp configuration")
parser.add_argument("--smtp", "-s", action="store", help="smtp server")
parser.add_argument("--port", "-p", action="store", type=int, help="smtp port")
parser.add_argument("--email", "-e", action="store", help="your email")
parser.add_argument("--password", "-pwd", action="store", help="your password")
parser.add_argument("--to", "-t", action="store", help="recipient")
parser.add_argument("--subject", "-sub", action="store", help="email subject")
parser.add_argument("--findMessage", "-fm", action="store", help="find a file message")
parser.add_argument("--message", "-m", action="store", help="message")
#Argument parsing
parser.parse_args()
args = parser.parse_args()
#Creating message


if args.libero and args.findMessage:
	with open (args.findMessage) as f :
		contents = str(f.readlines())
		#removing "[, ], '"
		contents = string.replace(contents, "[", "")
		contents = string.replace(contents, "]", "")
		contents = string.replace(contents, "'", "")
	#writing message	
	msg=MIMEText(contents)
	msg["Subject"] = args.subject
	msg["From"] = args.email
	msg["To"] = args.to
	#sending message
	email = smtplib.SMTP_SSL("smtp.libero.it", 465)
	email.login(args.email, args.password)
	email.sendmail(args.email, args.to, msg.as_string())
	print "done!"
	email.quit()
elif args.libero and args.message:
	#writing message
	msg=MIMEText(args.message)
	msg["Subject"] = args.subject
	msg["From"] = args.email
	msg["To"] = args.to
	#sending message
	email = smtplib.SMTP_SSL("smtp.libero.it", 465)
	email.login(args.email, args.password)
	email.sendmail(args.email, args.to, msg.as_string())
	email.quit()
	print "done!"
elif args.findMessage :	
	#open file
	with open (args.findMessage) as f :
		contents = str(f.readlines())
		#removing "[, ], '"
		contents = string.replace(contents, "[", "")
		contents = string.replace(contents, "]", "")
		contents = string.replace(contents, "'", "")
	#writing message	
	msg=MIMEText(contents)
	msg["Subject"] = args.subject
	msg["From"] = args.email
	msg["To"] = args.to
	#sending message
	email = smtplib.SMTP_SSL(args.smtp, args.port)
	email.login(args.email, args.password)
	email.sendmail(args.email, args.to, msg.as_string())
	print "done!"
	email.quit()
elif args.message :
	#writing message
	msg=MIMEText(args.message)
	msg["Subject"] = args.subject
	msg["From"] = args.email
	msg["To"] = args.to
	#sending message
	email = smtplib.SMTP_SSL(args.smtp, args.port)
	email.login(args.email, args.password)
	email.sendmail(args.email, args.to, msg.as_string())
	email.quit()
	print "done!"

