#import module or package to use its functions
import operations

from operations import subtraction

def main():
	print("3 + 5 = ", operations.addition(3, 5))
	print("8 x 2 = ", operations.multiplication(8, 2))
	print("10 - 2 = ", subtraction(10, 2))

#if current script is the main program
#if module is imported into another module,
#then __name__ == 'module_name'
if __name__ == '__main__':
	main()