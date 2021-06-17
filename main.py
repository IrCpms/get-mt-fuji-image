import urllib.request
from datetime import date, timedelta
from enum import Enum


class location(Enum):
    SHIMIZU = 'shimizu'
    FUJINOMIYA = 'fujinomiya'
    GOTENBA = 'gotenba'

  
def date_range(start, stop, step = timedelta(1)):
    current = start
    while current < stop:
        yield current
        current += step


for date in date_range(date(2021, 5, 30), date(2021, 5, 31)):
    date = date.strftime('%Y%m%d')

    for j in range(4, 20):
        if j < 10:
            j = "0" + str(j)

        url = "https://www.pref.shizuoka.jp/~live/archive/" + str(date) + location.SHIMIZU.value + "/" + str(j) + "/xl.jpg"
        
        # save
        save_name = date + "-gotenba-" + str(j) + "-xl.jpg"
        # Process
        urllib.request.urlretrieve(url, save_name)
        print(url, save_name)
