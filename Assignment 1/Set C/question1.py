#Write a Pandas program to get the day of month, day of year, week number and day of 
#week from a given series of date string.

import pandas as pd

dates = pd.Series([
    '2026-01-01',
    '2026-03-15',
    '2026-02-15'
])

dates = pd.to_datetime(dates, format='%Y-%m-%d')


print("Day:")
print(dates.dt.day)

print("Date of Year:")
print(dates.dt.dayofyear)

print("Week Number:")
print(dates.dt.isocalendar().week)

print("Day of Week:")
print(dates.dt.dayofweek)





