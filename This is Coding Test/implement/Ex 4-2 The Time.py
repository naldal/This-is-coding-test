n = int(input())

second, minute, hour, count = 0, 0, 0, 0
time = ''
while hour != n+1:
    time = str(hour)+str(minute)+str(second)
    second += 1

    if second == 60:
        minute += 1
        second = 0

    if minute == 60:
        hour += 1
        minute = 0

    if '3' in time:
        count += 1

print(count)
