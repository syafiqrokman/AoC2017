# sum = 0
# parse line by line
# 	parse currentNumber by currentNumber / seperated by space
# 		smallestNumber = first number
# 		biggestNumber = first number
# 		if currentNumber < smallestNumber
# 			smallestNumber = currentNumber
# 		if currentNumber > biggestNumber
# 			biggestNumber = currentNumber  
# 	sum = sum + (biggestNumber - smallestNumber) 

#maybe use CSV library?

sum = 0
number = []

file = open('day2input.txt')
for line in iter(file):
	int_line = [int (i) for i in line]


	number.append(line)    

print number[1]

file.close()