p=True
while(p):
	n=input()
	#print "n"
	#print n
	if(n==0.00):
		#print "0"
		break
	else:
		sum1=0.00
		#print "else-1"
		m=2.00
		while(True):
			#print "while-2"
			#print "m1"
			#print m
			sum1=sum1+float(1/m)
			#print "sum"
			#print sum1
			if(sum1>=n):
				#print "cond-arrived"
				#print n
				break
			else:
				m+=1
	print "%d card(s)"%int(m-1)