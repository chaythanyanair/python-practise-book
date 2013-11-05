#function to find duplicate elements in a list
def dups(x):
	p=[]
	for i in range(len(x)):
		j=i+1
		while j<len(x):	
			if x[i]==x[j]:
				p.append(x[j])
			j=j+1
	dupli=list(set(p))
	print dupli	

dups([1,2,3,3,2,4,5,3,2,4,5,5])
dups([9,1,2,2,4,5,3,2,4,5,5,0,0,100,100,9])


