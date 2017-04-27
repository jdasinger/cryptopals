
a = '1c0111001f010100061a024b53535009181c'
b = '686974207468652062756c6c277320657965'

def fixedXOR(a,b):
	x = int(a,16)
	y = int(b,16)
	return format((x^y), 'x')

print fixedXOR(a,b)