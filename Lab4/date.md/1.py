import datetime
x = datetime.datetime.today()
y = datetime.datetime.today() - datetime.timedelta(5)
print("5 days before: ", y)
print("Today: ", x)