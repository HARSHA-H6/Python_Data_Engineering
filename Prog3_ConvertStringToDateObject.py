import datetime

date_str = "12 Jun 2025"

print(f"Date as Date String: {date_str}")
print(type(date_str))

date_obj = datetime.datetime.strptime(date_str,"%d %b %Y")

print(f"Date as DateTime Object: {date_obj}")
print(type(date_obj))