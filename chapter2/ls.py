#sort strings based on lengths
def lensort(x):
	x.sort(key=lambda x:len(x))
	print x
lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])

	
	 
