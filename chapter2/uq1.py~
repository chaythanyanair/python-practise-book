#Improve the unique function written in previous problems to take an optional key function as argument and use the return value of the key function to check for uniqueness.
#>>> unique(["python", "java", "Python", "Java"], key=lambda s: s.lower())

def uniq(x,key=lambda x:x):
	p=[a for a in x for b in x if a!=b and a==key(a)]
	uq=list(set(p))
	print uq
uniq(["python", "java", "Python", "JAVA"], key=lambda s: s.upper())

