digits = {
    None: '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ',
}


separators = {
    None: '.',
}


def intLog(number, base):
    i = 0
    while base**i <= number:
        i += 1
    return i - 1


def setDigits(value, base=None):
    if base < 2:
        raise ValueError('Base must be at least 2.')
    digits[base] = str(value)


def setSeparators(value, base=None):
    if base < 2:
        raise ValueError('Base must be at least 2.')
    separators[base] = str(value)


def convert(value, initial, terminal, precision=0):
    return toBase(toNumber(value, initial), terminal, precision)


def toNumber(value, base):
    value = str(value)
    if base < 2 or type(base) != int:
        raise ValueError('Base must be an integer greater than or equal to 2.')
    d = base if digits.get(base) else None
    s = base if separators.get(base) else None
    decimal = value.find(separators[s])
    value = value.replace(separators[s], '')
    number = 0
    if (decimal == -1):
        i = len(value)
    else:
        i = decimal
    for char in value:
        i -= 1
        if digits[d].find(char) != -1 and digits[d].find(char) < base:
            number += digits[d].find(char) * base**i
    return number


def toBase(number, base, precision=0):
    if precision:
        number = float(number)
    else:
        number = int(number)
    if base < 2 or type(base) != int:
        raise ValueError('Base must be an integer greater than or equal to 2.')
    b = base if digits.get(base) else None
    s = base if separators.get(base) else None
    value = ''
    i = 0
    try:
        for i in reversed(xrange(precision + 1 + intLog(number, base))):
            x = int(number / base**(i - precision))
            number -= x * base**(i - precision)
            value += digits[b][x]
    except ValueError:
        value = digits[b][0]
    if precision:
        value = value[:len(value) - precision] + separators[s] + value[len(value) - precision:]
    return value
