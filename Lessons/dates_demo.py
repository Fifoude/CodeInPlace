import datetime

def do_datetime_stuff():
    # get current time
    now = datetime.datetime.now()
    print(now)

    # get the current time (formatted)
    now_formatted = now.strftime("%d/%m/%Y, %H:%M:%S")
    print(now_formatted)

    # get the current date
    today = datetime.date.today()
    today2 = today.strftime("%d/%m/%Y")
    print(today2)

    yesterday = today2 - datetime.timedelta(days=1)
    #print(yesterday)

do_datetime_stuff()