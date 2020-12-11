from datetime import datetime
from datetime import timedelta

last_time = datetime.now()
now_time = datetime.now()
print(type(now_time))
t = timedelta(seconds=10)
if last_time - t > now_time:
    print('ok')
else:
    print('no')
