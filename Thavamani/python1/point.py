class Point():

	__doc__ ="""A class implementation of a 2-dimensional point."""
     	def __init__(self,x,y):
      		self.x=x
      		self.y=y

	def __str__(self):
      		a=self.x
	      	b=self.y
      		x1=(a,b)
	      	return str(x1)
   
if __name__=='__main__':
	P1=Point(5,6)

	print str(P1.__doc__)
	
	