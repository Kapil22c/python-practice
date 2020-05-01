import re
import datetime
import pytz

#Regex with Python
#email address text scrapper
 
text="124544121 string"
pattern = re.compile("[a-zA-Z]+")
pattern1 = re.compile("[a-zA-Z0-9]+")

result= pattern.search(text)
result1=pattern1.search(text)
print(result)
print(result1)


txt="random string. MyName123@website.com. some more text. Your_Name.4-4-4@gim.com"
#pattern2=re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+")
pattern2=re.compile("[a-zA-Z0-9\.\-\_]+\@[a-zA-Z0-9]+\.[a-zA-Z]+")

result2=pattern2.search(txt)
result3=pattern2.findall(txt)
print(result2)
print(result3)

#date time module with python
# TASK: calculate the day between today and your birth day
# App that can send emails automatically based on date
# Insta post that say " posted 3 days ago"


today=datetime.date.today()
print(today)


birthday= datetime.date(1999, 7,13)
print((birthday))

days_b= (today-birthday).days
print(days_b)
# 10 days add or subract from current days

tdelta= datetime.timedelta(days=10)
print(today-tdelta)

print(today.month)
print(today.weekday())
#monday=0,...sunday=6

print(datetime.time(7, 2, 20, 15))
#datetime.date...(Y,M,D)
#datetime.time...(H,M,S,MS)
#datetime.datetime...(Y,M,D,h,m,s,ms)


# 10 hours to current time
hour_delta= datetime.timedelta(hours=10)
print(datetime.datetime.now()+hour_delta)

datetime_today=datetime.datetime.now(tz=pytz.UTC)
datetime_pacific =datetime_today.astimezone(pytz.timezone('Asia/Kolkata'))
print(datetime_pacific)

#for tz in pytz.all_timezones:  # all timezones available
#   print(tz)


#String formatting with dates
# 2020-03-28--> March 28, 2020
#strftime  :f-->formatting

print(datetime_pacific.strftime('%B %d, %Y'))

# March 28,2020 --> datetime(2020,3,28)
#strptime   :p-->parsing

datetime_thing=datetime.datetime.strptime('March 28, 2020','%B %d, %Y')
print(repr(datetime_thing))


# Use maya for the date time which i have downloaded







