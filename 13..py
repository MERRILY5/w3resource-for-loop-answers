n=5
k=n-1
p=1
for i in range(1,n):
    for j in range(1,k):
        print(end=" ")
    k=k-1
    for i in range(1,i+1):
        print(p ,end=" ")
        p+=1
    print("\r")
