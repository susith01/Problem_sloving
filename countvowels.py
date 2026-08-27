vowels = "aeiou"

letter = input("Enter the letter: ").lower()

if letter in vowels:
    print(len(letter))
else:
    print("The letter is not a vowel")