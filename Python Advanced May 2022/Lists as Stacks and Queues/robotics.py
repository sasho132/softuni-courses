from collections import deque

def time_in_seconds(time_data):
    time_in_seconds = 0
    hour, minutes, seconds = time_data.split(':')
    time_in_seconds += (int(hour) * 60 * 60) + (int(minutes) * 60) + int(seconds)
    return time_in_seconds 


def time_converter(seconds):
    hours = seconds // (60*60)
    seconds %= (60*60)
    minutes = seconds // 60
    seconds %= 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'
robots_data = input().split(';')

robots = {}
robots_processing_times = {}
time = time_in_seconds(input())
products = deque()

for robot in robots_data:
    name, process_time = robot.split('-')
    robots[name] =  int(process_time)
    robots_processing_times[name] = -1

current_product = input()
while current_product != 'End':
    products.append(current_product)
    current_product = input()

while products:
    time += 1
    current_product = products.popleft()

    for name, busy_time in robots_processing_times.items():
        if time >=  busy_time:
            print(f"{name} - {current_product} {time_converter(time)}")

