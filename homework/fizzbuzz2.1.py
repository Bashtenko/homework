fizz = int(input("enter number 1: "))
buzz = int(input("enter number 2: "))
n = int(input("enter number 3: "))
out = ""

i = 1
while i <= n:
	if i > 1:
		out += " "
	
	flag = True
	if i % fizz == 0:
		out += "F"
		flag = False
	if i % buzz ==0:
		out += "B"
		flag = False

	if flag:
		out += str(i)
	i += 1
print(out)
