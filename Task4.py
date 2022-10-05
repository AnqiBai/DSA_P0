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

numStat = dict()


def addRecord(numKey: str, numStat: dict(), tag: str):
    if numKey in numStat:
        if tag in numStat[numKey]:
            numStat[numKey][tag] += 1
        else:
            numStat[numKey][tag] = 1
    else:
        numStat[numKey] = dict()
        numStat[numKey][tag] = 1


# parse the raw data to get stat of each phone number
# calling, called, texting, texted
for record in calls:
    caller = record[0]
    callee = record[1]
    addRecord(caller, numStat, "calling")
    addRecord(callee, numStat, "called")


for record in texts:
    sender = record[0]
    receiver = record[1]
    addRecord(sender, numStat, "texting")
    addRecord(receiver, numStat, "texted")

# test the count of distinct phone numbers
# print(len(list(numStat.keys())))
# expect 570
print("These numbers could be telemarketers: ")
resultList = []
for num in numStat:
    curobj = numStat[num]
    if "calling" in curobj and "called" not in curobj \
            and "texting" not in curobj and "texted" not in curobj:
        resultList.append(num)

# sort and print
resultList.sort()
for num in resultList:
    print(num)
