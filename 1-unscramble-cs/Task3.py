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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# constants
BANGALORE = 3
FIXED_LINES = 0
TELEMARKETERS = 1
MOBILE = 2


def get_phone_type(number: str):
    if number.startswith('(080)'):
        return BANGALORE
    if number.startswith('(0'):
        return FIXED_LINES
    elif number.startswith('140'):
        return TELEMARKETERS
    else:
        return MOBILE


def task3a():
    codes = set()
    for call in calls:
        caller = call[0]
        if get_phone_type(caller) == BANGALORE:
            callee = call[1]
            phone_type = get_phone_type(callee)
            if phone_type == BANGALORE:
                codes.add(callee[1:4])
            elif phone_type == FIXED_LINES:
                end = callee.find(')')
                codes.add(callee[1:end])
            elif phone_type == TELEMARKETERS:
                codes.add(callee[:3])
            else:
                codes.add(callee[:4])

    print("The numbers called by people in Bangalore have codes:")
    codes = sorted(codes)
    for code in codes:
        print(code)


def task3b():
    to_bangalore_count = 0
    total_count = 0
    for call in calls:
        caller = call[0]
        if get_phone_type(caller) == BANGALORE:
            total_count += 1
            callee = call[1]
            if get_phone_type(callee) == BANGALORE:
                to_bangalore_count += 1

    percentage = round(((to_bangalore_count / total_count) * 100), 2)
    print(percentage, "percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


if __name__ == '__main__':
    task3a()
    task3b()
