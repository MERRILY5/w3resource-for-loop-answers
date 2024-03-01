num=int(input("Input upto the table number starting from 1: "))
print(f"Multiplication table from 1 to {num}")
for i in range(1,num+1):
    for j in range(1,11):
        print(f"{j} X {i} = {i*j}",end=" ")
    print()
    
    
    
