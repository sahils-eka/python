import json

dict1 = {1: {'id': '7jMjMcyt3qxEkbC0s8LJQf', 'name': 'Ghuroor', 'added_at': '2023-02-26T07:10:15Z', 'duration_sec': 198.857, 'popularity': 46, 'artists': [{'artist': 'Izzchughtai', 'artist_id': '211ei6ZiUeBMIXUZGBaJ4S'}, {'artist': 'Abdul Hannan', 'artist_id': '5mWQT8CLTa4mAQAJdFjHb1'}], 'genres': ['pakistani indie', 'pakistani pop']}}

mon = '05'
day = '01'
yr = '2020'
hr = '00'

for i in range(30):
    if int(hr) <= 23:
        hr = int(hr) + 1
    else:
        day = int(day) + 1
        hr = int(00)
    sn_end_time_format = f"{mon}/{day}/{yr} {hr}:03:23:000"
    print(sn_end_time_format)
