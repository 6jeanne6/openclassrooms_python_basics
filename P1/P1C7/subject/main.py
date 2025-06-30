fruits = {
	"apple": "red",
	"banana": "yellow",
	"orange": "orange"
}

print("Fruits dictionary: ", fruits)
fruits['kiwi'] = "green"
print("Fruits dictionary: ", fruits)

banana_color = fruits.get("banana")
print("Banana color = ", banana_color)

fruits['apple'] = "green"
print("Fruits dictionary: ", fruits)

fruits.pop("banana")
print("Fruits dictionary: ", fruits)

print("Fruits keys: ", fruits.keys())
print("Fruits values: ", fruits.values())
print("Fruits items: ", fruits.items())
print("Value for strawberry: ", fruits.get("strawberry"))
fruits.pop("orange")
print("Fruits dictionary: ", fruits)
fruits.clear()
print("Fruits dictionary: ", fruits)

print("Is there a banana? ", "banana" in fruits)
print("Is there a pear? ", "pear" in fruits)