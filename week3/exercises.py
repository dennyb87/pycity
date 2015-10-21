

def hi_fiven():

	'''
	Write a program that prompts the user to enter an integer.
	If the number is a multiple of 5, print HiFive.
	If the number is divisible by 2, print HiEven.
	'''

	user_string = input("Enter an integer: ")
	number = int(user_string)

	msg = "HiFive\n" if number % 5 == 0 else ""
	msg += "HiEven\n" if number % 2 == 0 else ""

	print(msg)



def math_learning_tool():

	'''
	This example creates a program to teach a child
	how to learn subtractions. The program randomly
	generates two single-digit integers number1 and
	number2 with number1 > number2 and displays a 
	question such as "What is 9 - 2?". After you type
	the answer in the input dialog box, the program
	displays a message dialog box to indicate whether
	the answer is correct.
	'''

	from random import randint

	number1 = randint(2, 9)
	number2 = randint(1, number1-1)
	question = "What is {} - {} ?\nAnswer: ".format(number1, number2)
	
	answer = input(question)
	solution = int(answer) == ( number1 - number2 )

	print("Your answer is {}".format(solution))



math_learning_tool()