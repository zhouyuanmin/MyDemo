"""
8. 使用time.time()方法能够得到目前的时间点，距离1970年1月1日0时0点0分0秒已经过去了多少秒。
已知，1970年1月1日星期四，使用计算机计算得出：
（1）今天距离1970年1月1日，过了多少天
（2）今天是星期几。
"""

import time
from datetime import datetime

times = int(time.time())
seconds = times % 60
hours = times // 3600
minutes = (times - hours * 3600) // 60
days = hours // 24
hours = hours - days * 24
print("从1970年到现在过去了", days, "天")

day_of_week = datetime.now().weekday()
week_map = {0: '一', 1: '二', 2: '三', 3: '四', 4: '五', 5: '六', 6: '日'}
print("星期" + week_map.get(day_of_week))
