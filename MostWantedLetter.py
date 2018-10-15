# Find the most frequent letter in the text. The letter returned must be in lower case.
# While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a".
# Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
#
# If you have two or more letters with the same frequency, then return the letter which comes first in the latin
# alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
#
# Input: A text for analysis as a string.
#
# Output: The most frequent letter in lower case as a string.

def checkio(text: str) -> str:
    # replace this for solution
    text = str.lower(text)

    text = text.replace(" ", "")
    text = text.replace("!", "")
    text = text.replace("?", "")
    text = text.replace(".", "")
    text = text.replace("0", "")
    text = text.replace("-", "")
    text = text.replace("1", "")
    text = text.replace("2", "")
    text = text.replace("3", "")
    text = text.replace("4", "")
    text = text.replace("5", "")
    text = text.replace(",", "")

    character_list = {}

    for number_of_characters in text:
        character_list[number_of_characters] = character_list.get(number_of_characters, 0) + 1

    maxValKey = max_in_order(character_list)

    return maxValKey


def max_in_order(char_list):
    max_value = max(char_list.values())
    max_char_list = []

    for letter in char_list:
        value = char_list.get(letter)
        if value == max_value:
            max_char_list.append(letter)

    max_char_list.sort()

    return max_char_list[0]

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))
    # self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("Passed all test lines.")