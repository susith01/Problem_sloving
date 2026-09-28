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

def square(num):
    return num*num
result = square(5)
print(result) #print the square of a number in function


def check_number(num):
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
num=int(input("Enter a number: "))
check_number(num) #print whether the number is even or odd in function


def count_vowels(text):
    vowels =input("Enter the vowels: ")
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

text = input("Enter a string: ")
vowel_count = count_vowels(text)
print(f"Number of vowels in '{text}': {vowel_count}") #print the number of vowels in a string in function

def count_vowels(text):
    
    a_count=0
    e_count=0
    i_count=0
    o_count=0
    u_count=0
    A_count=0
    E_count=0
    I_count=0
    O_count=0
    U_count=0
    for char in text:
        if char == 'a':
            a_count += 1
        elif char == 'e':
            e_count += 1
        elif char == 'i':
            i_count += 1
        elif char == 'o':
            o_count += 1
        elif char == 'u':
            u_count += 1
        elif char == 'A':
            A_count += 1
        elif char == 'E':
            E_count += 1
        elif char == 'I':
            I_count += 1
        elif char == 'O':
            O_count += 1
        elif char == 'U':
            U_count += 1
    return a_count, e_count, i_count, o_count, u_count, A_count, E_count, I_count, O_count, U_count

text = input("Enter a string: ")
vowels = input("Enter the vowels: ")
a_count, e_count, i_count, o_count, u_count, A_count, E_count, I_count, O_count, U_count = count_vowels(text)
print("a:", a_count)
print("e:", e_count)
print("i:", i_count)
print("o:", o_count)
print("u:", u_count)
print("A:", A_count)
print("E:", E_count)
print("I:", I_count)
print("O:", O_count)
print("U:", U_count)

def find_leargest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

print(find_leargest([1, 2, 32, 4, 5])) #print the largest number in a list in function

def second_larg(number):
    largest = second = float('-inf')
    for num in number:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second
print(second_larg([1, 2, 32, 4, 5])) #print the second largest number in a list in function