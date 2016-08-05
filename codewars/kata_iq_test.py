# coding=utf-8


def iq_test(numbers):
    list_iqtest = numbers.split()
    evens = True

    # check first 3 items for pattern, 2 odds or 2 evens determines "evens" value
    if int(list_iqtest[0]) % 2 is not 0 and int(list_iqtest[1]) % 2 is not 0:
        evens = False
    elif int(list_iqtest[1]) % 2 is not 0 and int(list_iqtest[2]) % 2 is not 0:
        evens = False
    elif int(list_iqtest[0]) % 2 is not 0 and int(list_iqtest[2]) % 2 is not 0:
        evens = False

    for i, n in enumerate(list_iqtest):
        # pattern evens=True
        if int(n) % 2 is not 0 and evens:
            return i + 1
        # pattern evens=False
        elif int(n) % 2 is 0 and not evens:
            return i + 1

# clever solution
def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1


# other ideas work in progress...
def iq_test(numbers):
    list_iqtest = numbers.split()
    evens, odds, index = (0, 0, 0)

    print(list_iqtest)

    for i, n in enumerate(list_iqtest):
        if int(n) % 2 is not 0:
            odds += 1
            index = i + 1
        else:
            evens += 1
            index = i + 1

        if evens > 2 or odds > 2:
            break

    return index



def iq_test(numbers):
    list_iqtest = numbers.split()
    print list_iqtest
    for i, n in enumerate(list_iqtest):
        if int(n) % 2 is not 0:
            return i + 1

Test.assert_equals(iq_test("2 4 7 8 10"), 3)
Test.assert_equals(iq_test("1 2 2"), 1)
Test.assert_equals(iq_test("5 3 2"), 3)


# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.
#
# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)
#
# Examples :
#
# iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even
#
# iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd