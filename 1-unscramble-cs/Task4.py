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


def task4():
    outgoing_calls = set([call[0] for call in calls])
    incoming_calls = set([call[1] for call in calls])

    in_out_texts = set([text[0] for text in texts] + [text[1] for text in texts])

    # outgoing_calls.difference(incoming_calls, outgoing_calls, incoming_texts)

    telemarketers = []

    for call in outgoing_calls:
        if call not in incoming_calls and call not in in_out_texts:
            telemarketers.append(call)

    telemarketers = sorted(telemarketers)
    print("These numbers could be telemarketers: ")
    for i in telemarketers:
        print(i)


if __name__ == '__main__':
    task4()
