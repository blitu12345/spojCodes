i=input()
ar=list(raw_input())
print ar
m=len(ar)
print m
k=0
p=i
while(p>0):
	j=k+1
	while(j<m+1):
		print ar[j-1]
		j+=i
	k+=1
	p-=1