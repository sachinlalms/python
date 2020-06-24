num = int(input("Enter the size of Row :"))
row = 0
while row < num:
    space = num-row-1
    while space>0:
        print(end=" ")
        space =space-1
    star=row+1
    while star>0:
        print("*", end=" ")
        star=star-1
    row=row+1
    print()
