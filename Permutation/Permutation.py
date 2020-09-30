
from itertools import permutations 

def allPermutations(str) 
	
	# Get all permutations of the string 
	permList = permutations(str) 

	# print all permutations 
	for perm in list(permList) 
		print (''.join(perm)) 
		
# Driver program 
if __name__ == __main__ 
	str = 'abcdefghijklmnopqrstuvwxyz'
	allPermutations(str) 
