# coding=utf-8

test_1 = "Sometimes (when I nest them (my parentheticals) too much (like this(and this))) they get confusing."


def paren_id(start, text):
    left_count = 0
    right_count = 0

    print(text[start:])

    for idx, char in enumerate(text[start:]):
        if char == "(":
            left_count += 1
        if char == ")":
            right_count += 1
        if left_count == right_count:
            return (idx + 1) + start
    if left_count < right_count:
        return -1
    else:
        return 1

print("10|79 = ", paren_id(10, test_1))
print("28|46 = ", paren_id(28, test_1))
print("57|78 = ", paren_id(57, test_1))
print("67|77 = ", paren_id(67, test_1))