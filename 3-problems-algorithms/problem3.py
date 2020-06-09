def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # Applying sorting functions below to input list
    input_list = sort_merged(input_list)

    # Instantiating sum values
    sum_1 = 0
    sum_2 = 0

    # Discerning the max sum values
    for i in range(len(input_list)):
        if i % 2 == 0:
            sum_1 = sum_1 * 10 + input_list[i]
        else:
            sum_2 = sum_2 * 10 + input_list[i]

    return [sum_1, sum_2]




def sort_merged(input_list):

    # Handling edge cases where input list is 0 or 1
    if len(input_list) <= 1:
        return input_list

    # Finding the middle of the list
    mid_index = len(input_list) // 2

    # Setting values less than or greater than that of the middle index
    left = input_list[:mid_index]
    right = input_list[mid_index:]

    # Using recursion to keep sorting list until "merge" condition is satisfied
    left = sort_merged(left)
    right = sort_merged(right)

    # Returning the value of the merge function
    return merge(left, right)

def merge(left, right):
    # Instantiating values
    merged = []
    left_index = 0
    right_index = 0

    # Iterating through inputs so long as inputs are greater than the instantiated left/right indices
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Adding values to overall merge list
    merged += left[left_index:]
    merged += right[right_index:]

    return merged

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

print('Printing the results of test 1:')
print('Values: [[1, 2, 3, 4, 5], [542, 31]]')
test_function([[1, 2, 3, 4, 5], [542, 31]])
print('\n')
print('Printing the results of test 2:')
print('Values: [[4, 6, 2, 5, 9, 8], [964, 852]]')
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
print('\n')
print('Printing the results of test 3:')
print('Values: [[3, 2, 6, 7, 9], [962, 73]]')
test_function([[3, 2, 6, 7, 9], [962, 73]])
# Adding edge test cases
print('\n')
print('Printing the results of test 4:')
print('Values: [[1, 2], [2, 1]]')
test_function([[1, 2], [2, 1]])
print('\n')
print('Printing the results of test 5:')
print('Values: [[1], [1]]')
test_function([[1], [1]])
