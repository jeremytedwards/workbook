# coding=utf-8

# Determine if a string has all unique characters?
# ?? ask ASCII or Unicode string, we'll assume ASCII


def unique_letters_in_ascii_string(test_string):
    if len(test_string) > 128:
        return False
    else:
        char_set = [False for x in range(128)]
        for char in test_string:
            if char_set[ord(char)]:
                return False
            else:
                char_set[ord(char)] = True


def unique_letters_in_ascii_string_sorting(test_string):
    # sort the string then walk to see if any neighbors match
    test_string.sort()
    for a, b in zip(test_string, test_string[1:]):
        if a == b:
            return False
    # no matches in test string
    return True


def unique_letters_in_ascii_string_with_set(test_string):
    # get a set of the string and compare lengths
    return len(set(test_string)) == len(test_string)


# Given two strings write a method to see if one is a permutation of the other.

def string_is_permutation(string_1, string_2):
    # If they are permutations then they have the same characters in different orders
    # Sort the two strings and compare
    # sorted() creates new strings and does not mutate
    # string_1.sort() would mutate
    return sorted(string_1) == sorted(string_2)
