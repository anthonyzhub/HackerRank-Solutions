#! /usr/bin/python3

"""

Task: Sort a list in ascending order by the element's absolute value. If two or more elements share the same absolute value, then sort them with numeric sign included

Ex. 

Input: [0, -9, 3, 3, -1, -1, 0]
Output: [0, 0, -1, -1, 3, 3, -9]

"""

from collections import Counter

def bubblesort(arr):

    # Keep track of many duplicates there are
    a_dict = Counter(arr)

    # Get absolute value of each element inside of list
    arr = list(map(abs, (i for i in arr)))

    # Sort list
    arr.sort()

    # Iterate list
    for i in range(len(arr)):

        curr_key = arr[i] * -1

        # Check if key exist and has a value greater than 1
        if a_dict[curr_key]:

            # Flip sign
            arr[i] = arr[i] * -1

            # Decrement value
            a_dict[curr_key] -= 1

    return arr

if __name__ == "__main__":
    
    arr = [0, -9, 3, 3, -1, -1, 0]

    print(arr)
    print(bubblesort(arr))
