# Let's suppose our monkeys are typing, typing and typing, and have produced a wide variety of short text segments.
# Let's try to check them for sensible word inclusions.

# You are given some text potentially including sensible words.
# You should count how many words are included in the given text.
# A word should be whole and may be a part of other word. Text letter case does not matter.
# Words are given in lowercase and don't repeat. If a word appears several times in the text, it should be counted only once.

# For example, text - "How aresjfhdskfhskd you?", words - ("how", "are", "you", "hello"). The result will be 3.

# Input: Two arguments. A text as a string (unicode for py2) and words as a set of strings (unicode for py2).

# Output: The number of words in the text as an integer

def count_words(text: str, words: set) -> int:
    text = text.lower()
    number_words_occurred = 0

    for word in words:
        index_start = 0
        found_index = -2

        found_index = text.find(word, index_start)
        if found_index != -1:
            number_words_occurred += 1
            index_start = found_index + 1

    print(number_words_occurred)

    return number_words_occurred

if __name__ == '__main__':
    # self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Booom! Passed all test lines")