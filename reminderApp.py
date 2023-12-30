import schedule
import time as tm
from datetime import time, timedelta, datetime

'''
The aim of this project is to emulate a reminder app using python. This python file therefore needs to stay active indefinitely in order to remind as desired.
I've added functions that contain reminders of actions i do on a timely basis
'''
def proofOfFunction():
    print("This prints every 3 seconds as proof that it works")
    
def hydrate():
    print("Drink Water Now!")

def fit():
    print("Do 25 pushups, 20 sit-ups, 20 jumping jacks")

def edu():
    print("Practice some code")

'''
The functions here are passed as objects instead of being called, and contained in them are print statements relevant to the reminders
'''
schedule.every(3).seconds.do(proofOfFunction)
schedule.every().hour.do(hydrate)
schedule.every(4).hours.do(fit)
schedule.every(3).hours.do(edu)

#The scheduled tasks are applied using the method below to run the scheduling
while True:
        schedule.run_pending()
        tm.sleep(1)



    

    
        

    
    

   