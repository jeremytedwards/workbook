# coding=utf-8

def make_readable(seconds):
    mm, ss = divmod(seconds, 60)
    hh, mm = divmod(mm, 60)
    return '%02d:%02d:%02d'%(hh, mm, ss)

# Other examples:
#     def make_readable(s):
#         return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)



# Description:
#
# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
#
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)
#
# You can find some examples in the test fixtures.

# Test.assert_equals(make_readable(0), "00:00:00")
# Test.assert_equals(make_readable(5), "00:00:05")
# Test.assert_equals(make_readable(60), "00:01:00")
# Test.assert_equals(make_readable(86399), "23:59:59")
# Test.assert_equals(make_readable(359999), "99:59:59")