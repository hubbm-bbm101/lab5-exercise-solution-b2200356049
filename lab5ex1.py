N=int(input("Enter a number: "))
sumodds=0
sumevens=0
numofevens=0
numofodds=0
for i in range(1,N+1):
    if i%2==0:
        sumevens+=i
        numofevens+=1
    else:
        sumodds+=i
        numofodds+=1
        
print("Sum of odds: ",sumodds/numoffodds)
print("Average of evens: ",sumevens/numofevens)        
