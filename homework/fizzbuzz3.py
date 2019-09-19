"""fizz = int(input("enter number 1: "))
buzz = int(input("enter number 2: "))
n = int(input("enter number 3: "))"""

import sys
in_filename = sys.argv[1]
out_filename = sys.argv[2]
in_file = open(in_filename, "r")
out_file = open(out_filename, "w")
for line in in_file:
	numbers = line.split()
	fizz = int(numbers[0])
	buzz = int(numbers[1])
	n = int(numbers[2])

	out = ""
	i = 1
	while i <= n:
		if i > 1:
			out += " "
		if i % fizz == 0 and i % buzz == 0:
			out += "FB"
		else: 
			if i % fizz == 0:
				out += "F"
			elif i % buzz ==0:
				out += "B"
			else:
				out += str(i)
		i += 1
	print(out)
	out_file.write(out + "\n")
in_file.close()
out_file.close()