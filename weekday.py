# week 5 task
# program that outputs the day of the week
# and outputs a message based on the day of the week

# import datetime module
import datetime 

# use the now() method of the datetime class for today's date & time
now = datetime.datetime.now()

# use weekday() method to return day of the week
# 0 = Monday ..... 7 = Sunday
weekday = now.weekday()

# dictonary for the days of the week
days_of_the_week = {0:"Monday", 1:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}

# print day of the week in text
print("Today is", days_of_the_week[weekday])

# if statement to returning weekday string (Monday to Friday)
if weekday in range(0,5):
    print("Yes, unfortunately today is a weekday.")

# else statement to return weekend statement (Saturday & Sunday)
else:
    print("It is the weekend, yay!")
