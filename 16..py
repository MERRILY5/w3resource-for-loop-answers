num=int(input("Input number of terms: "))
total=0
even=0
for i in range(1,num+1):
    even=(2*i)
    total+=even
print(f"The Sum of even Natural Number upto {num} terms : {total}")
