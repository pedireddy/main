a=int(input())
b=int(input())

for n in range(a+1,b):
	sum=0
	temp=n
	while temp > 0 :
		r=temp%10
		sum=sum+(r**3)
		temp=temp//10
	if sum==n:
		print(sum)
