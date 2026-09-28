name=str(input("Enter the name: "))
print(len(name))                                                      #1

a="susith"
print(a[::-1])                                                        #2

word="Hii susith welcome"
print(len(word.split()))                                              #3

string=str(input("Enter the string: "))
reverse=string[::-1]
if string==reverse:
    print("The string is palindrome")
else:
    print("The string is not palindrome")                              #4   
    

name = input("Enter the name: ")
vowels = input("Enter the vowels: ")
count = 0

for char in name:
    if char in vowels:
        print(char)
        count += 1

print("Total vowels:", count)                                          #5

name=input("Enter the name: ")
a_count=0
e_count=0
i_count=0
o_count=0
u_count=0
n_count=0
for char in name:
    if char=="a":
        a_count+=1
    elif char=="e":
        e_count+=1
    elif char=="i":
        i_count+=1
    elif char=="o":
        o_count+=1
    elif char=="u":
        u_count+=1   
    else:
        n_count+=1

print("A:", a_count)
print("E:", e_count)
print("I:", i_count)
print("O:", o_count)
print("U:", u_count)
print("Not a vowel:", n_count)                                         #6