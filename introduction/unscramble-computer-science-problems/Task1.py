"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
telephone_set = set()
for sending_num , receiving_num, time in texts:
    telephone_set.add(sending_num)
    telephone_set.add(receiving_num)

for calling_num , receiving_num, time, during in calls:
    telephone_set.add(calling_num)
    telephone_set.add(receiving_num)

print(f"There are <{len(telephone_set)}> different telephone numbers in the records.")
