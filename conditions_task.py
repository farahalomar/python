first_number = raw_input("Enter your first number: ")
second_number = raw_input("Enter your second number: ")
operation = raw_input("Choose your operation (+, -, /, *): ")
if first_number.isdigit() and second_number.isdigit() == False:
        print("The numbers were invalid")
elif first_number.isdigit() and second_number.isdigit() == True:
        if operation == "+":
                answer = int(first_number) + int(second_number)
        elif operation == "-":
                answer = int(first_number) - int(second_number)
        elif operation == "/":
                answer = int(first_number) / int(second_number)
        elif operation == "*":
                answer = int(first_number) * int(second_number)
        elif operation != "+" and operation != "-" and operation != "/" and operation != "*":
                print("The operation choice is invalid")
        print(answer)
