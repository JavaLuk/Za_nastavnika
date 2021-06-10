#Bernulijev niz: (1,2,3,5,8,13,...) #?Valjda?#
s = 1
lista = [1, 2]

x = int(input("Unesi mesto u nizu: "))
for z in range((x-2)):
	s = (lista[len(lista)-1]+lista[len(lista)-2])
	lista.append(s)

print(lista)