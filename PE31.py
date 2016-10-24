coinlist=[1,2,5,10,20,50,100,200]

def number_ways_to_make_change(cents, coins):
	if cents==0:
		return 1
	elif cents<0:
		return 0
	else:
		total=0
		for i in range(len(coins)):
			total+=number_ways_to_make_change(cents-coins[i],coins[0:i+1])
		return total

print number_ways_to_make_change(200, coinlist)
