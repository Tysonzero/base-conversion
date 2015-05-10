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
    digits[int(base)] = str(value)


def setSeparators(value, base=None):
    separators[int(base)] = str(value)


def toNumber(value, base):
    value = str(value)
    base = int(base)
    d = base if digits.get(base) else None
    s = base if separators.get(base) else None
    decimal = value.find(separators[s])
    decimal = len(value) - 1 if decimal == -1 else decimal - 1
    value = value.replace(separators[s], '')
    number = 0
    for i, char in enumerate(value):
        if digits[d].find(char) != -1 and digits[d].find(char) < base:
            number += digits[d].find(char) * base**(decimal - i)
    return number


def toBase(number, base, precision=0):
    number = float(number) if precision else int(number)
    base = int(base)
    d = base if digits.get(base) else None
    s = base if separators.get(base) else None
    value = ''
    i = 0
    try:
        for i in reversed(xrange(precision + 1 + intLog(number, base))):
            x = int(number / base**(i - precision))
            number -= x * base**(i - precision)
            value += digits[d][x]
    except ValueError:
        value = digits[d][0]
    if precision:
        value = value[:len(value) - precision] + separators[s] + value[len(value) - precision:]
    return value


def convert(value, initial, terminal, precision=0):
    return toBase(toNumber(value, initial), terminal, precision)
