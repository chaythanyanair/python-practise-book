#function to compute factorial
def fact(x):
	f=1
	for a in range(x+1):
		if a!=0:
			f=f*a
	print 'factorial is:',f

fact(4)
fact(0)
fact(1)
		
