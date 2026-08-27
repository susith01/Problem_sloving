list_numbers=[23,5,67,45,12]  #Without using any function
largest=list_numbers[0]
two_largest=list_numbers[1]
for number in list_numbers:
    if number>largest:
        largest=number
    elif number>two_largest and number!=largest:    
        two_largest=number
print(two_largest)