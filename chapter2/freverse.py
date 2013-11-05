#to print lines of a file in reverse order
def lrev(filename):
	f=open(filename).readlines()
	f.reverse()
	for lines in f:	
		print lines

lrev('temp.txt')
