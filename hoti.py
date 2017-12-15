for i in range(input()):
	n = input()
	a=[];b=[]
	a=map(int,raw_input().split())
	b = map(int, raw_input().split())
	a=sorted(a)
	b=sorted(b)
	count = 0
	for i in range(n):
		count = count+a[i]*b[i]
	print count