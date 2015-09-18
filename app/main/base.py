
def encode(num):
	'''Turns a database primary_key for a URL into a shortcode'''

	alphabet = '23456789bcdfghjkmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ-_'
	
	#padding to avoid one letter urls
	#num += len(alphabet)

	if num == 0:
		return 0
	base = len(alphabet)
	
	shortcode = ""
	while num > 0:
		rem = num % base
		shortcode += alphabet[rem]
		num /= base
	return shortcode

def decode(string):
	'''Turns a short URL code into a database primary_key num'''

	alphabet = '23456789bcdfghjkmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ-_'
	alphalen = len(alphabet)

	return sum([alphabet.index(char) * pow(alphalen, power) for power, char in enumerate(reversed(string))])
