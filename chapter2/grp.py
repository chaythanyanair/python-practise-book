#Write a function group(list, size) that take a list and splits into smaller lists of given size.
#>>> group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def group(List,size):
	if size<=len(List):
		i=0
		while i<len(List):
			p=List[i:i+size]
			i=i+size
			print p

group([1,2,3,4,5,6,7,8,9],3)
group([1,2,3,4,5,6,7,8,9],4)
group([1,2,3,4,5],4)
