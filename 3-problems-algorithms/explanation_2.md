# Problem 2

This one is also making use of a binary search algorithm
to produce a rotated sorted array.
Based on a few conditions on how a produced middle index value
compares to the left and right extremities of the array,
we continue to perform iterations by appropriately
decrementing / incrementing the extremities of the array
until we finally get down to some final indices and
then comparing them appropriately.
Time complexity is O(logn). Space complexity is O(1) since we do not use additional space
