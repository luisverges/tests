def collatz():
	number= int(input("Enter number\n"))
	while number != 1:
		if number % 2== 0:
			number = number//2
		else:
			number = 3*number + 1
		print(number)
collatz()
input("Press enter to exit")
