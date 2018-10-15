

''' Used the slice method on a LIST to split it into 2 parts and compare them against each other to return Bool'''

# 1st part targets the start of the list(list[1:]
# 2nd part targets the end of the list(list[:-1])
# using the return method compare the 1st part the list to the 2nd (return list[1:] == list[:-1])
#EXAMPLE
    #List = [1, 2, 3, 4]

    # def all_the_same(elements):
        #return list[1:] == list[:-1]
#>>>[1, 2, 3]
#>>>[2, 3, 4]

def all_the_same(elements):
    return elements[1:] == elements[:-1]

if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # self-checking and not necessary for auto-testing
    assert all_the_same([1, 1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Passed all test lines")