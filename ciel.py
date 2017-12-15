a,b=raw_input().split()
c = list(str(int(a)-int(b)))
n = len(c)
if(c[n-1]!="2"):
	c[n-1]="2"
else:
	c[n-1]="1"
print ''.join(c)