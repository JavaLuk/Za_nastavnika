#trazi rec u unesenoj reci(inp)
def trazi(inp, rec, x, d, z):
	y = 0
	while x!=d:
		if inp[(x+z)]==rec[x]:
			y+=1
		x+=1
	print(y)
	return y
	
inp = input("Unesi reč: ")
rec = input("Unesi rec-u-rec: ")

b = (len(inp)-1)
d = (len(rec)-1)

x = 0
z = 0

if b<d:
	print("Nemoguće naći veću reč u manjoj reči!!!")
else:
	while trazi(inp, rec, x, d, z)!=d:
		trazi(inp, rec, x, d, z)
		z+=1
	print("Nadjeno ", (trazi(inp, rec, x, d, z)+1), " slova od reci: ", rec)
	