import re

def getinput():
	print('1)Binary\n2)Octal\n3)Decimal\n4)Hexadecimal')
	validated = False
	while validated == False:	
		inputanswer = input('What number system are you inputting? ')
		validated = validate(inputanswer, validated)

	validated = False
	while validated == False:
		outputanswer = input('What number system would you like to get back? ')
		validated = validate(outputanswer, validated)
		
	return inputanswer, outputanswer


def validate(answer, validated):
	if re.search('[^1-4]$', answer):
		print('INVALID INPUT: Please enter a number between 1 and 4!')
	else:
		validated = True

	return validated


def getdecimalnumber():
	decimal = input('Please enter your decimal number: ')
	decimal = int(decimal)
	
	return decimal

def binarytodecimal():
	binary = input('Please enter your binary number: ')
	binary = binary.replace(' ', '')
	decimal = int(binary, 2)
	
	return decimal


def octaltodecimal():
	octal = input('Please enter your octal number: ')
	decimal = int(octal, 8)

	return decimal


def hextodecimal():
	hex = input('Please enter you hexadecimal number: ')
	decimal = int(hex, 16)
	
	return decimal


def decimaltobinary(decimal):
	binary = bin(decimal)[2:]
	
	print('Your Binary number is: ', binary)


def decimaltooctal(decimal):
	octal = oct(decimal)[2:]
	
	print('Your Octal number is: ', octal)


def decimaltohex(decimal):
	hexa = hex(decimal)[2:]
	
	print('Your Hexadecimal number is: ', hexa)
	
inputanswer, outputanswer = getinput()

if inputanswer == '1':
	decimal = binarytodecimal()
elif inputanswer == '2':
	decimal = octaltodecimal()
elif inputanswer == '4':
	decimal = hextodecimal()
else:
	decimal = getdecimalnumber()
	
if outputanswer == '1':
	decimaltobinary(decimal)
elif outputanswer == '2':
	decimaltooctal(decimal)
elif outputanswer == '3':
	print('Your Decimal number is: ', decimal)
else:
	decimaltohex(decimal)
