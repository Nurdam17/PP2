import datetime
today = datetime.datetime.today()
yesterday = today - datetime.timedelta(1)
tomorrow = today + datetime.timedelta(1)
print("Yesterday: ", yesterday)
print("Today: ", today)
print("Tomorrow ", tomorrow)