from datetime import datetime, timedelta

# 1
date1 = datetime.fromisoformat("2023-11-27 20:34:13.212967")
print(date1 + timedelta(weeks=1))

# 2
date2 = datetime.fromisoformat("2023-07-15 18:25:10.121473")
weekdays = {
    0: "понедельник",
    1: "вторник",
    2: "среда",
    3: "четверг",
    4: "пятница",
    5: "суббота",
    6: "воскресенье",
}
print(weekdays[date2.weekday()])

# 3
date3 = datetime.fromisoformat("2023-06-12 15:23:45.312167")
days_ago = (datetime.now() - date3).days
print(days_ago)
