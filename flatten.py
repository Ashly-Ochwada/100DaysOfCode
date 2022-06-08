list = [[1,20] ,[3,4] ,[5,6]]
y=[]
y = [x for sublist in list for x in sublist]
print(y)

marks = [75, 86,99,56,78]
sum = 0
for m in marks:
    sum = sum + m
print(sum)    

n = 1
while n <10:
    if n==5:
        n=n+1
        continue
print(n) 
n = n+1  