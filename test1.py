#A vendor has 9 apples hes willing to give to you, he counts apples, ask how many you want, then responds based on user input
for i in range(0,10): #He's not smart he has to count them individually
	if(i == 1):
		print("i have " + str(i) + " apple") #exception for 1 apple
	else:
		print("i have " + str(i) + " apples")  #everything else
print("how many apples do you want?")
a = input() #let him know how many you want
if(int(a) < 10): #make sure he has the apples u want
	print("alright, here you go")
else: #you asked for too many
	print("I don't have that many apples")

	
