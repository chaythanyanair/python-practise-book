#Write a function extsort to sort a list of files based on extension.
def extsort(x):
	p=[]
	exsorted=[]
	for a in x:
		p.append(a.split('.'))
	p.sort(key=lambda x:x[1])
	for a in p:
		exsorted.append('.'.join(a))
	print exsorted	
extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])

