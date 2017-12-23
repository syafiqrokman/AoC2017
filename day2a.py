input_file = open('day2input.txt')

sum = 0
for line in iter(input_file):
	values_in_line = line.split()
	smallestNumber = 99999
	biggestNumber = 0
	for currentNumber in values_in_line:
		if int(currentNumber) <= smallestNumber:
			smallestNumber = int(currentNumber)
		if int(currentNumber) >= biggestNumber:
			biggestNumber = int(currentNumber)  
	sum = sum + (biggestNumber - smallestNumber) 
print sum


input_file.close()


   




