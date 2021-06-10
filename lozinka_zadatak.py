# Unesi neku lozinku po volji (Može da se sastoji od velikih i maljih slova i brojeva)
loz = input("Unesi pravu lozinku: ")
# Daj nekom drugom da pogodi lozinku 
# (npr. lozinka je 'LuKa123', onaj ko pogađa može da napiše 'luka123' i pogodi će)
rec = input("Unesi lozinku(proba): ")

while True:
	if rec.upper()==loz.upper():
		break
	else:
		rec = input("Unesi lozinku(proba): ")
print("Pogodak!")