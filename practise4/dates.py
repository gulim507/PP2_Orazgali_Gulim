#1.

import datetime

today = datetime.datetime.now()
print(today)


# 2

import datetime

today = datetime.datetime.now()

print(today.month)
print(today.day)


# 3

import datetime

birthday = datetime.datetime(2008, 7, 15)
print(birthday)


# 4

import datetime

date = datetime.datetime(2024, 3, 10)

print(date.strftime("%B"))
