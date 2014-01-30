import math

digits = {
	0:'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ',
	2:'01',
	10:'0123456789',
	16:'0123456789ABCDEF',
}

def setDigits(value, base=0):
	if base < 0 or base == 1:
		raise ValueError, 'Base must be an integer greater than or equal to 2 or 0 to set default.'
	digits[base] = value

def convert(value, initial, terminal):
	return fromNumber(toNumber(value, initial), terminal)

def toNumber(value, base):
	if int(base) < 2 or int(base) != base:
		raise ValueError, 'Base must be an integer greater than or equal to 2.'

	value = str(value)
	number = 0
	i = 0

	for char in reversed(value):
		if digits.find(char) != -1 and digits.find(char) < base:
			number += digits.find(char) * base**i

		i += 1

	return number


def fromNumber(number, base):
	if int(base) < 2 or int(base) != base:
		raise ValueError, 'Base must be an integer greater than or equal to 2.'

	value = ''
	i = 0

	try:
		for i in reversed(xrange(1 + int(round(math.log(number, base), 10)))):
			x = int(number / base**i)
			number -= x * base**i
			value += digits[x]
	except ValueError:
		value = '0'

	return value