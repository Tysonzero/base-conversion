import math


digit_strings = {
    0: '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ',
}


def set_digits(value, base=0):
    digit_strings[int(base)] = str(value)


def to_number(value, base):
    value = str(value)
    base = int(base)
    digit_string = digit_strings.get(base) or digit_strings[0]
    number = 0
    for i, char in enumerate(reversed(value)):
        if digit_string.find(char) != -1 and digit_string.find(char) < base:
            number += digit_string.find(char) * base**i
    return number


def to_base(number, base):
    number = int(number)
    base = int(base)
    digit_string = digit_strings.get(base) or digit_strings[0]
    value = ''
    try:
        for i in reversed(xrange(1 + int(round(math.log(number, base), 10)))):
            x = int(number / base**i)
            number -= x * base**i
            value += digit_string[x]
    except ValueError:
        value = digit_string[0]
    return value


def convert(value, initial, terminal):
    return to_base(to_number(value, initial), terminal)
