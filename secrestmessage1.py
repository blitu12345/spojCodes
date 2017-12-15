while(True):
	n=input()
	if(n==0):
		break
	else:
		ar=list(raw_input())
		ar_new=[]
		m=len(ar)
		p=m/n
		k=n-1
		for i in range(n):
			for j in range(p):
				if(j%2==0):
					#print ar[i+j*n],
					ar_new.append(ar[i+j*n])
				else:
					#print ar[i+j*n+k],
					ar_new.append(ar[i+j*n+k])
			k-=2
		print ''.join(ar_new)
