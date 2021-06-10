def krov(broj):
	for x in range(broj):
		print(" "*((broj-x)//2), "# "*(x+1), " "*((broj-x)//2))

def body(broj):
	for y in range(broj):
		print(" 0"*broj)

def kuca(broj):
	krov(broj)
	body(broj)

kuca(5)