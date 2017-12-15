while(True):
	n=input()
	if(n==0):
		break
	else:
		sum1 = 0
		while(n>0):
			sum1+=n*n
			n-=1
		print sum1