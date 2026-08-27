num = [10,20,30,10,20,30,40,50]
for i in num:
    if i==10:
        print(i)
    elif i==20:
        print(i)
    elif i==30:
        print(i)
    elif i==40:
        print(i)
    elif i==50:
        print(i)
        
num = [10,20,30,10,20,30,40,50]     
unique_num = []
for i in num:
    if i not in unique_num:
        unique_num.append(i)
print(unique_num)                