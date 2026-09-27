from datetime import datetime, timedelta

# 1. Subtract five days
today = datetime.now()
five_days_ago = today - timedelta(days=5)
print(five_days_ago)

# 2. Yesterday, today, tomorrow
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

# 3. Drop microseconds
without_microseconds = today.replace(microsecond=0)
print(without_microseconds)

# 4. Difference between two dates in seconds
date1 = datetime(2026, 9, 20)
date2 = datetime(2026, 9, 27)

difference = date2 - date1
print(difference.total_seconds())