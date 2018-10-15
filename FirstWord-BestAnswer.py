# BestVoted Answer at checkio - similar to my solution

def first_word(text: str) -> str:
    """ returns the first word in a given text."""

    text = text.replace('.', ' ').replace(',', ' ').strip() # used .replace and .strip in same way
    return text.split()[0]# difference between my code and this return text.split()and requesting first item in list [0]

if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    #self-checking and not necessary for auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Passed all test lines!")