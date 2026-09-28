name = input("Enter the name: ")
vowels = input("Enter the vowels: ")
count = 0

for char in name:
    if char in vowels:
        print(char)
        count += 1

if letter in vowels:
    print(len(letter))
else:
    print("The letter is not a vowel")