t=input()
while(t>0):
	t-=1
	raw_input()
	n=input()
	i1=0;a=[0]*n
	while(i1<n):
		a[i1]=input()
		i1+=1
	i1=0;count=0
	while(i1<n-1):
		i2=i1+1
		while(i2<n):
			if(a[i1]>a[i2]):
				count+=1
			i2+=1
		i1+=1
	print count