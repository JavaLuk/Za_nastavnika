def linija(times, text):
	if text=="":
		print("*"*times)
	else:
		print(text[0]*times)

linija(5, "=")
linija(5, "Lol")
linija(4, "")
#Output:

# =====
# LLLLL
# ****