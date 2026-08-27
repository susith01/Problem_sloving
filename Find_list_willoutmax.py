list_number=[23,5,67,45,12]
list_number.sort()
print(list_number[-1])      #using sort function

list_numbers=[23,5,67,45,12]  #Without using any function
largest=list_numbers[0]
for number in list_numbers:
    if number>largest:
        largest=number
print("Largest:", largest)