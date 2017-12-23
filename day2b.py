input_file = open('day2input.txt')

sum = 0
for line in iter(input_file):
	values_in_line = line.split()

	for currentNumber in values_in_line:
		for nextNumber in values_in_line:
			if int(currentNumber) == int(nextNumber):
				break
			if int(currentNumber)%int(nextNumber)==0:
				sum = sum + (int(currentNumber)/int(nextNumber))
			elif int(nextNumber)%int(currentNumber)==0:
				sum = sum + (int(nextNumber)/int(currentNumber))

print sum
input_file.close()


   




