def maximum(a,b,c):
	""" largest of 3
	numbers
	"""
	if a>b and a>c:
		return a
	elif b>c:
		return b
	else:
		return c

a=input("Enter A")
b=input("Enter B")
c=input("Enter C")

max=maximum(a,b,c)
print max

