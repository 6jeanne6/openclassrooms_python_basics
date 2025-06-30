#list
fruits = ["apple", "banana", "orange"]
print("Fruits list: ", fruits)

fruits.append("kiwi")
print("Fruits list: ", fruits)

fruits.remove("orange")
print("Fruits list: ", fruits)

fruits.insert(1, "pineapple")
print("Fruits list: ", fruits)

print("Length of fruits list = ", len(fruits))

fruits.sort()
print("Fruits list after sort: ", fruits)

print("Occurence of strawberry: ", fruits.count("strawberry"))
berry = ["strawberry", "raspberry", "blueberry", "blackberry"]
fruits.extend(berry)
print("Fruits list: ", fruits)
print("Occurence of pineapple: ", fruits.count("pineapple"))
print("Which index is kiwi: ", fruits.index("kiwi"))

#tuple
standard_tuning = ["E", "A", "D", "G", "B", "E"]
print("Standard tuning: ", standard_tuning)
print("Is E in standard_tuning: ", "E" in standard_tuning)
print("Is T in standard_tuning: ", "T" in standard_tuning)
