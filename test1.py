for i in range(0,10):
	if(i == 1):
		print("i have " + str(i) + " apple")
	else:
		print("i have " + str(i) + " apples")
print("how many apples do you want?")
a = input()
if(int(a) < 10):
	print("alright, here you go")
else:
	print("I don't have that many apples")

	
