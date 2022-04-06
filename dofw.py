# import the required modules
from datetime import date
import calendar
import string
# get the date input from user 
dt = input("Find out what day of the week was your birthday.  Enter the date in dd/mm/yyyy format : ")
wkday = dt.split("/")
# print day for actual birthday
curr_date = date(int(wkday[2]), int(wkday[1]), int(wkday[0]))
print((int(wkday[2])), calendar.day_name[curr_date.weekday()])
#print day for last 10  years
todays_date = date.today()
thisyear = todays_date.year
print ("Past 10 years of birthdays: ")
i = 1
for i in range(10):
    curr_date = date(thisyear - i, int(wkday[1]), int(wkday[0]))
    print((thisyear - i), calendar.day_name[curr_date.weekday()])
