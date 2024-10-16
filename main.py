import time

currentSecond = str(time.time())

listSecond = []

listSecond = currentSecond.split('.')

unique = listSecond[0] + listSecond[1]

print(unique)