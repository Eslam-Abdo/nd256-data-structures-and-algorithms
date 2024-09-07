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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
calling_num_set = set()
telemarketers = set()

for calling_num , receiving_num, time, during in calls:
    telemarketers.add(calling_num)

for sending_num , receiving_num, time in texts:
    if sending_num in telemarketers or receiving_num in telemarketers:
        telemarketers.discard(sending_num)
        telemarketers.discard(receiving_num)

for calling_num , receiving_num, time, during in calls:
    if receiving_num in telemarketers:
        telemarketers.discard(receiving_num)

telemarketers = list(telemarketers)
telemarketers.sort()
print("These numbers could be telemarketers: ")
for tele in telemarketers:
	print(tele)