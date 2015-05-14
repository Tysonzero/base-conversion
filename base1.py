import math


digit_strings = {
    0: '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ',
}


def set_digits(value, base=0):
    digit_strings[int(base)] = str(value)


def to_number(value, base):
    value = str(value)
    base = int(base)
    number = 0
    b = 0

    if digit_strings.get(base, ''):
        b = base

    for i, char in enumerate(reversed(value)):
        if digit_strings[b].find(char) != -1 and digit_strings[b].find(char) < base:
            number += digit_strings[b].find(char) * base**i

    return number


def from_number(number, base):
    number = int(number)
    base = int(base)
    value = ''
    i = 0
    b = 0

    if digit_strings.get(base, ''):
        b = base

    try:
        for i in reversed(xrange(1 + int(round(math.log(number, base), 10)))):
            x = int(number / base**i)
            number -= x * base**i
            value += digit_strings[b][x]
    except ValueError:
        value = digit_strings[b][0]

    return value


def convert(value, initial, terminal):
    return from_number(to_number(value, initial), terminal)
