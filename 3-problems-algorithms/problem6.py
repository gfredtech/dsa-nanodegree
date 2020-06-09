import random

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) <= 0:
        return 'List is empty.'
    # Instantiating min / max values as positive / negative infinity, respectively
    min_val = float('inf')
    max_val = - float('inf')

    # Iterating through inputted integers
    for int in ints:
        # Setting new max_val if int value is higher
        if int > max_val:
            max_val = int
        # Setting new min_val if int value is lower
        if int < min_val:
            min_val = int

    print(f'Minimum: {min_val}')
    print(f'Maximum: {max_val}')

    return min_val, max_val

# TESTS
print('Test 1')
print('Values 0-9 Shuffled:')
l = [i for i in range(0, 10)]
random.shuffle(l)
print(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print('\n')
print('Test 2')
print('Values 33-54 Shuffled:')
l = [i for i in range(33, 55)]
random.shuffle(l)
print(l)
print ("Pass" if ((33, 54) == get_min_max(l)) else "Fail")
print('\n')
print('Test 3')
print('Values 100-125 Shuffled:')
l = [i for i in range(100, 126)]
random.shuffle(l)
print(l)
print ("Pass" if ((100, 125) == get_min_max(l)) else "Fail")
print('\n')
print('Test 4')
print('Values "Null":')
l = []
print("Pass" if (get_min_max(l) == 'List is empty.') else "Fail")
print('\n')
print('Test 5:')
print('Values "Null":')
l = []
print("Pass" if (get_min_max(l) == 'List is empty.') else "Fail")
