import datetime, bday_messages

today = datetime.date.today()
next_birthday = datetime.date(2025, 11, 10)
time_left = (next_birthday - today).days

if time_left == 0:
    msg = bday_messages.random_message
    print(msg)
else:
    print(f"My next birthday is {time_left} days aways!")