# coding=utf-8


def my_parse_int(string):
    string.replace(" ", "")
    try:
        number = int(string)
        return number
    except ValueError:
        return "NaN"


# def my_parse_int(string):
#     result = "NaN"
#     for i in string:
#         if i.isspace() or i.isdigit():
#             if i.isdigit():
#                 print(i)
#                 result = int(i)
#             continue
#
#     return result
#
#
# def my_parse_int(string):
#     if any(c.isalpha() for c in string):
#         return "NaN"
#     else:
#         item = [int(i) for i in string if i.isdigit() ]
#         return item[-1] if item else "NaN"


# JavaScript provides a built-in parseInt method.
#
# It can be used like this:
#
# parseInt("10") returns 10
# parseInt("10 apples") also returns 10
# We would like it to return "NaN" (as a string) for the second case because the input string is not a valid number.
#
# You are asked to write a myParseInt method with the following rules:
#
# It should make the conversion if the given string only contains a single integer value (and eventually spaces - including tabs, line feeds... - at both ends)
# For all other strings (including the ones representing float values), it should return NaN
# It should assume that all numbers are not signed and written in base 10