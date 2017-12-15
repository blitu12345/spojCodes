def cloumn1(sum):
	n=0
	p=True
	while(p):
		if(sum<=n*(n+1)/2):
			p=False
			return n
		else:
			n+=1

for i in range(input()):
	sum1=input()
	n=cloumn1(sum1)
	#print "n"
	#print n
	count=n*(n-1)/2
	#print "count"
	#print count
	if(n%2==0):
		#print "if-1"
		a=1
		b=n
		p=True
		#print "a"
		#print a
		#print "b"
		#print b
		while(p):
			#print "while-1"
			#print "count-while"
			#print count
			if(count==sum1-1):
				p=False
				print "TERM %d IS %d/%d" %(sum1,a,b)
			count+=1
			a+=1
			b-=1
		#print "while-end"

	elif(n%2!=0):
		#print "if-2"
		b=1
		a=n
		p=True
		#print "a1"
		#print a
		#print "b1"
		#print b
		while(p):
			#print "while2-1"
			#print "count2-while"
			#print count
			count+=1
			b+=1
			a-=1
			if(count==sum1-1):
				p=False
				print "TERM %d IS %d/%d" %(sum1,a,b) 
		#print "while-end2"		