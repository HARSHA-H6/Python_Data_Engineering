import datetime

def display_datetime():
    
    now = datetime.datetime.now()
    print(f'Current Date time: {now}')
    print("Formateed Date and Time")


    print(f"Month : {now.strftime('%B')}")
    print(f"Weekday : {now.strftime('%A')}")
    print(f"Year : {now.strftime('%Y')}")
    print(f"Month in abbrivated form: {now.strftime('%b')}")
    print(f"Weekday in abbrivated form:{now.strftime('%a')}")
    print(f"Year as two digit: {now.strftime('%y')}")
    print(f"present date: {now.strftime('%D')}")
    print(f"Date of the month: {now.strftime('%d')}")
    print(f"Month : {now.strftime('%m')}")
    print(f"Hour in 24 hour clock: {now.strftime('%H')}")
    print(f"Hour in 12 hours format: {now.strftime('%I')}")
    print(f"Minutes : {now.strftime('%M')}")
    print(f"AM/Pm indicator: {now.strftime('%p')}")

display_datetime()