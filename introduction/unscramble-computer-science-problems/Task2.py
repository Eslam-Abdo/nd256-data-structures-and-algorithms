"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
telephone_number = dict()
for calling_num , receiving_num, time, during in calls:
    telephone_number[calling_num] = int(during) + telephone_number.get(calling_num,0)
    telephone_number[receiving_num] = int(during) + telephone_number.get(receiving_num,0)

max_during = 0
max_tele = None

for tele , during in telephone_number.items():
    if during > max_during:
        max_during = during
        max_tele = tele
print(f"<{max_tele}> spent the longest time, <{max_during}> seconds, on the phone during September 2016.")
