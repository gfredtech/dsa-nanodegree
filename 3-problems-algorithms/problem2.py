def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    # Instantiating indices based on input_list
    left_index = 0
    right_index = len(input_list) - 1

    # Iterating search proper results are generated
    while right_index > left_index + 1:

        # Determining the middle index position
        mid_index = (left_index + right_index) // 2

        # Determining next array to search based on appropriate condition
        if input_list[left_index] < input_list[mid_index] < input_list[right_index]:
            if number > input_list[mid_index]:
                left_index = mid_index
            else:
                right_index = mid_index

        elif input_list[mid_index] > input_list[left_index] and input_list[mid_index] > input_list[right_index]:
            if input_list[left_index] <= number < input_list[mid_index]:
                right_index = mid_index
            else:
                left_index = mid_index

        elif input_list[mid_index] < input_list[left_index] and input_list[mid_index] < input_list[right_index]:
            if input_list[mid_index] < number <= input_list[right_index]:
                left_index = mid_index
            else:
                right_index = mid_index

    # Performing comparison between final remaining indices
    if input_list[left_index] == number:
        return left_index
    elif input_list[right_index] == number:
        return right_index
    else:
        return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# Adding edge cases
test_function([[1], 1])
test_function([[-1], -1])
