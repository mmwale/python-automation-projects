import requests
import schedule 
import time as tm
from datetime import time, timedelta, datetime


'''
This project combines concepts of scheduling and requests from functions in python. It acts as a reminder for every period of time to send emails using mailgun's api.
'''
#variables containing Mailgun api key and directory
MAILGUN_API_ENDPOINT = "https://api.mailgun.net/v3/sandbox48f18bb892ea48a2b833acce78fdc831.mailgun.org/messages"
MAILGUN_API_KEY = 'fac6450c9b38af6a19bf155db2728573-7ecaf6b5-0d0a17da'

#defined a function to send the email reminder
def send_email(to, subject, body):
    #a data object that contains information about the required email reminder
    data = {
		'from': 'mwalemedan@gmail.com',
		'to': to,
		'subject': subject,
		'text': body
	}
    #created a variable response that relays data to the Mailgun API 
    response = requests.post(
		MAILGUN_API_ENDPOINT,
		auth=('api', MAILGUN_API_KEY),
		data=data
	)
    #posed an if-else statement to check the status of the email sending attempt
    if response.status_code == 200:
        print("Email sent!")
    else:
        print("Unsuccessful")

#Created data used in the variables of the data object that correspond with the Mailgun account 
to = "Medani Mwale <mwalemedan@gmail.com>"
subject = 'Reminder'
body = "This is to remind you to finish that project"
schedule.every(10).seconds.do(send_email, to, subject, body)#schedule package being implemented to call the email function every 10 seconds

'''
in the event you wish to not have a scheduled send, stop the program, delete the scheduler above and
replace it with the send_email function call below. That way, running the program will only execute the function once 
as it is only called once.
'''
#send_email(to, subject, body)

#defined a while statement that enables the schedule package to execute. The time package acts as a default to delay execution every given number of seconds
while True:
    schedule.run_pending()
    tm.sleep(1)
