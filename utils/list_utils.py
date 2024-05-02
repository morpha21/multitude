def splitter(elements, quantity):
	return [
		[
			elements[j]
			for j in range(i, len(elements), quantity)
			if j < len(elements)
		]
		for i in range(0,quantity)
	]


if __name__ == "__main__":
	lista = [i for i in range(1, 28)]
	for i in splitter(lista, 4):
		print(i)
