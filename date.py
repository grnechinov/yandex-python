import datetime as dt


n = int(input())
interval = dt.timedelta(days=n)
date1 = dt.date(2019, 9, 1)
date2 = date1 + interval
print(date2.day, date2.month)
