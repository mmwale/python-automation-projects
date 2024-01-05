import datetime

file = open (r'C:\Users\HEWLETT PACKARD\python-workspace\Projects\reminderWhileCoding.txt', 'a')#function that opens the directory containing the named txt file to be used in the task scheduling

file.write(f'{datetime.datetime.now} - Drink some water \n')#method that writes onto the named txt file defined in the previous function 