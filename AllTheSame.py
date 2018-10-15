# check if all elements in the given list are equal.
# Input: List.
# Output: Bool.

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:

    for e in elements: #loop over the list
        if e != elements[0]: #checking if every element in list matches the 1st element if not return False
            return False #return Bool
    return True #return Bool

if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # self-checking and not necessary for auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Passed all test lines")