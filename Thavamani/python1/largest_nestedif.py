def maximum(a,b,c):
	""" largest of 3
	numbers
	"""
	if a>b:
		if a>c: 
			return a
		else:
			return c
	elif b>c:
		return b
	else:
		return c

a=input("Enter A")
b=input("Enter B")
c=input("Enter C")

max=maximum(a,b,c)
print max

