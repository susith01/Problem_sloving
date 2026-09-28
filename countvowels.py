name = input("Enter the name: ")
vowels = input("Enter the vowels: ")
count = 0

for char in name:
    if char in vowels:
        print(char)
        count += 1

print("Total vowels:", count)