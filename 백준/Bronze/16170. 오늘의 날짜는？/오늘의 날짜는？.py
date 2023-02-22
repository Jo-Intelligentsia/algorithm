from datetime import datetime, timedelta
now = datetime.now() -timedelta(hours=9)
print(now.year)
print(now.month)
print(now.day)