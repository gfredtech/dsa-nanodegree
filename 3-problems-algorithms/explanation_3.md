# Problem 3

For this particular problem,
we're taking in an inputted list,
and with the assistance of two helper functions,
we appropriately sort the inputted list without
making use of Python's default `sort()` function.
These helper functions move values to the left or right
of the middle index value and keeps iterating through this list until
we have a fully sorted list.
We then iterate through the sorted values to pull out the
max sum values.
Time complexity is O(nlogn) (due to merge_sort)
and space complexity is O(n)
