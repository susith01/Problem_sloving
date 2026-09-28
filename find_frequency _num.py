num = [1,2,3,2,1,2,3,4,1]
count_1=0
count_2=0
count_3=0
count_4=0
for i in num:
    if i==1:
        count_1+=1
    elif i==2:
        count_2+=1
    elif i==3:
        count_3+=1
    elif i==4:
        count_4+=1
print("1:", count_1)
print("2:", count_2)
print("3:", count_3)    
print("4:", count_4)        


num = [10, 20, 10, 30, 20, 40, 10, 50]

frequency = {}

for i in num:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print(frequency)

