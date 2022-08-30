"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
from datetime import datetime
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


def stringToDatetime(inputstr):
    return datetime.strptime(inputstr, '%d-%m-%Y %H:%M:%S')


def datetimeToString(inputDatetime):
    return inputDatetime.strftime('%d-%m-%Y %H:%M:%S')


# look for first record of texts:
incNum1 = texts[0][0]
ansNum1 = texts[0][1]
mintime1 = stringToDatetime(texts[0][2])
for record in texts:
    currentRecordTime = stringToDatetime(record[2])
    if currentRecordTime < mintime1:
        incNum1 = record[0]
        ansNum1 = record[1]
        mintime1 = currentRecordTime

mintimeStr1 = datetimeToString(mintime1)
print('First record of texts, %s texts %s at time %s' %
      (incNum1, ansNum1, mintimeStr1))


# look for last record of calls:
incNum2 = calls[0][0]
ansNum2 = calls[0][1]
maxtime2 = stringToDatetime(calls[0][2])
lastimeStr = calls[0][3]
for record in calls:
    currentRecordTime = stringToDatetime(record[2])
    if currentRecordTime > maxtime2:
        incNum2 = record[0]
        ansNum2 = record[1]
        maxtime2 = currentRecordTime
        lastimeStr = record[3]

maxtimeStr2 = datetimeToString(maxtime2)
print('Last record of calls, %s calls %s at time %s, lasting %s seconds' %
      (incNum2, ansNum2, maxtimeStr2, lastimeStr))

# Time Complexity:
# O(n)
# since both record lists are traversed once.
