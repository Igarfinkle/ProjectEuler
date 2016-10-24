import itertools
def convert(tupl):
	total=0
	power=0
	for char in tupl:
		total+=int(char)*(10**power)
		power+=1
	return total

sum=0
for perm in itertools.permutations('0123456789'):
	if (convert(perm[6:9])%2==0 
		and convert(perm[5:8])%3==0 
		and convert(perm[4:7])%5==0 
		and convert(perm[3:6])%7==0
		and convert(perm[2:5])%11==0
		and convert(perm[1:4])%13==0
		and convert(perm[0:3])%17==0):
		print convert(perm[0:3])
		print convert(perm)
		sum+=convert(perm)
print sum
