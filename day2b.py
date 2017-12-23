#clean coding

def isSameNumber(number_x,number_y):
	if number_x == number_y:
		return True
	else:
		return False

def isEvenlyDivisible(numerator,denominator):
	if numerator%denominator == 0:
		return True
	else:
		return False
		
# def updateSumIfEvenlyDivisible

input_file = open('day2input.txt')

sum = 0
for line in iter(input_file):
	values_in_line = line.split()

	for currentNumber in values_in_line:
		for nextNumber in values_in_line:
			if isSameNumber(currentNumber,nextNumber) == True:
				break
			if isEvenlyDivisible(int(currentNumber),int(nextNumber)):
				sum = sum + (int(currentNumber)/int(nextNumber))
			if isEvenlyDivisible(int(nextNumber),int(currentNumber)):
				sum = sum + (int(nextNumber)/int(currentNumber))
print sum
input_file.close()


   




