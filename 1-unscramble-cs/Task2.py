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


def task2():
    distinct = set()
    for call in calls:
        distinct.add(call[0])
        distinct.add(call[1])

    dictionary = {number: 0 for number in distinct}
    for call in calls:
        dictionary[call[0]] += int(call[3])
        dictionary[call[1]] += int(call[3])

    max_seconds = max(dictionary, key=dictionary.get)
    print(max_seconds, "spent the longest time,", dictionary[max_seconds], "seconds, on the phone during September "
                                                                           "2016.")


if __name__ == '__main__':
    task2()
