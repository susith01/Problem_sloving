number=[10,15,20,23,30]
odd=0
even=0
for i in number:
    if i%2==0:
        print("even",i)
    
        #even+=1
    else:
        print("odd",i)
       # odd+=1
        
print("Total odd numbers in the list are:",odd)
print("Total even numbers in the list are:",even)        