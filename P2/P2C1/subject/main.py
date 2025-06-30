import sys

number1 = input("Enter a number: ")
number2 = input("Enter a number: ")

#isnumeric() = check that all characters in string are numeric characters
if number1.isnumeric() and number2.isnumeric():
	print("Both numbers are numeric")
	number1 = int(number1)
	number2 = int(number2)
else:
	raise SystemExit("Your numbers are not numeric")

operation = input("Choose an operation: + - * /")
match operation:
		case "+":
			result = number1 + number2
		case "-":
			result = number1 - number2
		case "*":
			result = number1 * number2
		case "/":
			if number2 == 0:
				raise SystemExit("Cannot divide by 0")
			result = number1 / number2
			round(result)
		case _:
			raise SystemExit("Invalid operation")

if result > sys.maxsize:
	raise SystemExit("Int overflow detected")
elif result < -sys.maxsize - 1:
	raise SystemExit("Int overflow detected")

print(f"{number1} {operation} {number2} = {result}")