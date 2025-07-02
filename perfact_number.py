num=int(input("Plese enter the number. :- "))
i=1
sum=0
while i<num:
    if num%i==0:
        sum+=i
    i+=1
if sum==num:
    print(num," Is Prfact number.")
else:
    print(num,"is not a perfact number.")