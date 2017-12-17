n=int(input())
a=0
b=1
print(a)
print(b)
count=0
if n<0:
	print("enter positive numbers only")
else:
	while count<n-2:
		c=a+b
		a=b
		b=c
		count+=1
		print(c)
