first_number = float(raw_input("Enter your first number: "))
second_number = float(raw_input("Enter your second number: "))
operation = raw_input("Choose your operation (+, -, /, *): ")
if first_number != float() and second_number != float():
	print("The numbers were invalid")
elif first_number == float() and second_number == float():
	if operation == "+":
		answer = first_number + second_number
	elif operation == "-":
		answer = first_number - second_number
	elif operation == "/":
               	answer = first_number / second_number
	elif operation == "*":
               	answer = first_number * second_number
	elif operation != "+" or "-" or "/" or "*":
		print("The operation choice is invalid")
	print("Your answer is", answer)
