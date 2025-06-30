#handling lists and data with loops
numbers = input("Insert a number list separated by , example: 1,2,3,4\n")
list = numbers.split(',')
print(f"Here is your list: {list}")
int_list = []
for x in list:
	int_list.append(int(x))
	print("Int list: ", int_list)

#could use sum()
sum = 0
for s in int_list:
	sum += s
print(f"Sum = {sum}")

average = sum / len(int_list)
print(f"Average is = {average}")

superior_list = []
for y in int_list:
	if y > average:
		superior_list.append(y)
print(f"Numbers that are superior than the average: ", len(superior_list))
print(f"These numbers are: {superior_list}")