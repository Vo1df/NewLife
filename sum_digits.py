# sum_digits.py

import sys

def sum_of_digits(number):
    try:
        number = int(number)
        if 10 <= number <= 99:
            tens = number // 10
            units = number % 10
            return tens + units
        else:
            return 'Error: Please enter a two-digit number.'
    except ValueError:
        return 'Error: Invalid number format.'

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python sum_digits.py <two_digit_number>")
    else:
        number = sys.argv[1]
        print(sum_of_digits(number))