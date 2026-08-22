city=input("Enter your city name:")
temp=float(input("Enter the temperature in your country:"))

if temp >40:
    print("Warning it it very hot today")

if temp>25:
    print("Have a nice day")
else:
    print("Grab a jacket")

if temp>45:
    print("Weather:Scorching hot")
elif temp>35:
    print("Weather:Nice and Sunny")
elif temp>25:
    print("Weather:A little cold")
else:
    print("Weather: Very chilly")

import datetime as dt
import calendar as c

now=dt.datetime.now()
print("City:", now)
print("Time:", now)

print(c.calendar(now.year))