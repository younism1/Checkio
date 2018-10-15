# Find the length of the longest substring that consists of the same letter.
# For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa". The last
# substring is the longest one which makes it an answer.

# Input: String.

# Output: Int.

def long_repeat(line):
    """length the longest substring that consists of the same char"""
    occured_number = 0
    character_occured = "dummy"

    max_number = 0

    for character in line:

        if character_occured != character: #
            if max_number <= occured_number:
                max_char = character_occured
                max_number = occured_number

            character_occured = character
            occured_number = 1

        else:
            occured_number += 1

    if max_number <= occured_number:
        max_char = character_occured
        max_number = occured_number

    return max_number

if __name__ == '__main__':
    # self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('Passed all test lines')