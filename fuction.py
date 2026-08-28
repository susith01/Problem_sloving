def my_function():
    print("hello")
my_function()     #print the hello in function

def add(a,b):
    return a+b
print(add(10,20)) #print the sum of two numbers in function

def for_loop(num):
    for i in range(1,num+1):
        print(i)
        
for_loop(5) #print the numbers from 1 to 5 in function        

def while_loop(num):
    i=1
    while i<=num:
        print(i)
        i+=1
        
while_loop(5) #print the numbers from 1 to 5 in function        