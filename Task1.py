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
numberSet = set()

for record in texts:
    numberSet.add(record[0])
    numberSet.add(record[1])

for record in calls:
    numberSet.add(record[0])
    numberSet.add(record[1])

print("There are %d different telephone numbers in the records." % len(numberSet))

# Time Complexity:
# average: O(n)
# Since the average time complexity of the set add method is O(1), and both lists are traversed.
