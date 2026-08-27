num=int(input())
even=[]
odd=[]
for i in range(1,num+1):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
        
print("Even numbers are:",even,len(even))
print("Odd numbers are:",odd,len(odd))        