def remove_zero(a):
	if(a[0]=='0'):
		a.remove(a[0])
		remove_zero(a)
	else:
		print ''.join(a)


def reverse_fun(a):
	a = list(a)
	n1 = len(a)
	n2 = 0
	c = "2"
	if( n1%2==0 ):
		while(n2<n1/2):
			c=a[n2]
			a[n2]=a[n1-1-n2]
			a[n1-1-n2]=c
			n2+=1
	else:
		while(n2<(n1-1)/2):
			c=a[n2]
			a[n2]=a[n1-1-n2]
			a[n1-1-n2]=c
			n2+=1
	return(a)

for i in range(input()):
	a ,b= (raw_input().split())
	a = reverse_fun(a)
	b = reverse_fun(b)
	c = int(''.join(a))+int(''.join(b))
	c = list(str(c))
	c=reverse_fun(c)
	remove_zero(c)