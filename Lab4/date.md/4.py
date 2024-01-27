import datetime
x = datetime.datetime.today()
date1 = x
y = input() #2024-01-26 00:00:00
date2 = datetime.datetime.strptime(y, '%Y-%m-%d %H:%M:%S')
def dif(date1, date2):
    difference = date1 - date2
    return difference.days * 24 * 3600 + difference.seconds
print(date1)
print(date2)
print(dif(date1, date2))