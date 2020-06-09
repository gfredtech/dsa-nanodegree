def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    # Handling cases for negative numbers
    if number < 0:
        return 'Please enter a positive number.'

    # Handling cases where number is 0 or 1
    if number == 0 or number == 1:
        return number

    # Instantiating start and end numbers
    start = 0
    end = number // 2

    # Applying search algorithm to calculate square root
    while start <= end:

        # Finding the middle between start and end, then squaring it
        middle = (start + end) // 2
        middle_squared = middle * middle

        # Checking to see if middle_squared matches the input number; else increments appropriately
        if middle_squared == number:
            return middle
        elif middle_squared < number:
            start = middle + 1
            result = middle
        else:
            end = middle - 1

    return result

# Running Problem 1 Tests
# Printing test results
print ('Test 1: Square root of 9')
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ('Test 2: Square root of 0')
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ('Test 3: Square root of 16')
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ('Test 4: Square root of 1')
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ('Test 5: Square root of 27')
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# Adding edge cases
# Adding edge case tests
print ('Test 6: Square root of -1')
print ("Pass" if  ('Please enter a positive number.' == sqrt(-1)) else "Fail")
print ('Test 7: Square root of -100')
print ("Pass" if  ('Please enter a positive number.' == sqrt(-100)) else "Fail")
