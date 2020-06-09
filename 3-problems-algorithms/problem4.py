def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    for i in input_list:
        if i > 2 or i < 0:
            return 'Cannot process list.'


    # Instantiating array index values
    min_val = 0
    mid_val = 0
    max_val = len(input_list) - 1

    # Iterating while max_val is greater than or equal to mid_val
    while mid_val <= max_val:

        # Handling condition where mid_val is 0
        if input_list[mid_val] == 0:
            # Flip-flopping min and mid values
            input_list[min_val], input_list[mid_val] = input_list[mid_val], input_list[min_val]

            # Incrementing min and mid indicies
            min_val += 1
            mid_val += 1
            continue

        # Handling condition where mid_val is 2
        elif input_list[mid_val] == 2:
            # Flip-flopping mid and max values
            input_list[mid_val], input_list[max_val] = input_list[max_val], input_list[mid_val]

            # Decrementing max index
            max_val -=1
            continue

        # Handling any other condition
        else:
            mid_val += 1
            continue

    return input_list

def test_function(test_case):
    # Printing original values
    print('Original Values: ')
    print(test_case)

    # Sorting values with function
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Test Passed!")
    elif sorted_array == 'Cannot process list.':
        print("Test Passed!")
    else:
        print("Test Failed!")


print('Test Case 1:')
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
print('\n')
print('Test Case 2:')
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
print('\n')
print('Test Case 3:')
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
print('\n')
print('Test Case 3:')
test_function([-1])
print('\n')
print('Test Case 4:')
test_function([4])
