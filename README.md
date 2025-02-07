# Triple-Sum-Optimization

This program is written to test a possible optimization for the triple sum problem. 

The triple sum problem involves finding three numbers in a list that add up to a given target sum. Given an array of integers and a target sum, the goal is to determine if there are three distinct elements in the array whose sum is equal to the target sum.

## Algorithms

\* *Note: Each of these algorithms assumes the list is pre-sorted* \*

### Default Binary Search Algorithm
This algorithm uses the first two loops in the brute force search, and then uses a binary search to check for the negative of the sum of the two values. If `-(array[i] + array[j])` exists in the list, then there is a solution.


### Skip Search Optimization
This algorithm is the same as the default algorithm above, however before checking to see if the array holds the value `-(array[i] + array[j])` it checks to see if the current `-sum` is within the bounds of the sorted array.

### Trim Optimization
This optimization is a pre-optimization, reducing the size of the list to remove any unusable values. This works by checking the top 2 and bottom 2 values (referred to as the max and min respectively). If the max is greater than the min, then values might be able to be trimmed off the lower end of the array, and so a binary search is used.
```
min = array[0] + array[1]
max = array[size - 1] + array[size - 2]

if min > max + THRESHOLD
    # trim any values past -min on the top end of the array
if min > max + THRESHOLD
    # trim any values past -max on the bottom end of the array
```