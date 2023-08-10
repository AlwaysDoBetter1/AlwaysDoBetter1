'''
A natural number is being processed. You need to write a program that displays
the maximum digit of a number that is a multiple of 33. If there are no digits
divisible by 33 in the number, you need to display "NO" on the screen. The programmer
was in a hurry and wrote the program incorrectly.

Find all the errors in this program (there are exactly 55 of them).
It is known that each error affects only one line and can be fixed without
changing other lines.

Note 1. The number 00 is divisible by any natural number.
Note 2: If necessary, you can add the necessary lines of code.
'''
n = int(input())
max_digit = -1
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:
            max_digit = digit
    n = n // 10
if max_digit == -1:
    print('NO')
else:
    print(max_digit)