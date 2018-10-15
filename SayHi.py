# In this mission you should write a function that introduce a person with a given parameters in attributes.

# Input: Two arguments. String and positive integer.

# Output: String.


def say_hi(name: str, age: int) -> str:
    """ Hi! """
    return "Hi. My name is {} and I'm {} years old".format(name, age)

if __name__ == '__main__':
    # self-checking and not necessary for auto-testing
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"
    print('Done, passed test lines.')