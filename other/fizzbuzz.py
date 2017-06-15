# coding=utf-8

# given a range of numbers:
# - print out "Fizz" if the number is mod 3
# - print out "Buzz" if it is mod 5
# - print out "FizzBuzz" if mod by both
# - print out the number if mod neither

for num in range(1, 50):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


