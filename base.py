import math

DIGITS = {
	0:'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ',
	2:'01',
	10:'0123456789',
	16:'0123456789ABCDEF',
}

def convert(value, initial, terminal):
	return fromNumber(toNumber(value, initial), terminal)

def toNumber(value, base):
	value = str(value)
	number = 0
	i = 0

	for char in reversed(value):
		if DIGITS.find(char) != -1 and DIGITS.find(char) < base:
			number += DIGITS.find(char) * base**i

		i += 1

	return number


def fromNumber(number, base):
	value = ''
	i = 0

	try:
		for i in reversed(xrange(1 + int(round(math.log(number, base), 10)))):
			x = int(number / base**i)
			number -= x * base**i
			value += DIGITS[x]
	except ValueError:
		value = '0'

	return value