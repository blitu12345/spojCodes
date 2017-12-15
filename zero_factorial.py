def factorial(n):
	f=1
	while(n>0):
		f=f*(n)
		n-=1
	return(f)


for i in range(input()):
	n=(factorial(input()))
	p=0
	while(n%10==0):
		p=p+1
		n=n/10
	print p
