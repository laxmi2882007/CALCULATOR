#store the two numbers from user input
#float() allows the program to accept both whole numbers and decimals
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

#perform addition and subtraction
sum_result = num1 + num2
diff_result = num1 - num2

#Display the results
print(f"the sum of {num1} and {num2} is: {sum_result}")
print(f"the difference when subtracting {num2} from {num1} is: {diff_result}")

