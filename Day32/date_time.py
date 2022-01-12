# Day32 of my 100DaysOfCode Challenge
# using datetime module

import datetime as dt

# gets current date and time
now = dt.datetime.now()
print(now)

# can access a specific part from date time like year, month, weekday, etc.
year = now.year
print(year)

# use datetime to store date.time of birth
date_of_birth = dt.datetime(year=1995, month=12, day=10, hour=13, minute=45, second=33)
print(date_of_birth)

