# coding=utf-8

# Example 1
import itertools


# The following function returns the longest palindrome contained in a given string.
def is_palindrome(s):
    return s == s[::-1]


def longest_palindrome(s):
    s = s.lower()
    longest = ""
    for id_y, item_y in enumerate(s):
        for id_x, item_x in enumerate(s):
            check = s[id_y:id_x+1].lower()
            if is_palindrome(check) and (len(check) > len(longest)):
                longest = check
    return longest

print("iTopiNonAvevanoNipoti = ", longest_palindrome("iTopiNonAvevanoNipoti"))
print("onAvevano - ", longest_palindrome("iGattiNonAvevanoCugini"))


# Example 2
# Look at all the substrings of a given string and check them individually
# text.index() will only find the first occurrence of the longest palindrome,
# so if you want the last, replace it with text.rindex()
def palindromes(text):
    text = text.lower()
    results = []

    for i in range(len(text)):
        for j in range(0, i):
            chunk = text[j:i + 1]

            if chunk == chunk[::-1]:
                results.append(chunk)

    return text.index(max(results, key=len)), results


print("iTopiNonAvevanoNipoti - ", palindromes("iTopiNonAvevanoNipoti"))
print("onAvevano - ", palindromes("iGattiNonAvevanoCugini"))