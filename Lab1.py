from random import randint

arr=[[randint(0,100) for i in range (6)] for j in range (10)]

print("Do sortirovki")

for i in range(10):
    for j in range(6):
        print(arr[i][j],end=" ")
    print()
    
print()

n=6*10

st=[0]*n

k=0

for i in range(10):
    for j in range(6):
        st[k]= arr[i][j]
        k=k+1

for i in range(n-1):
    for j in range(n-i-1):
        if st[j] > st[j+1]:
            st[j], st[j+1] = st[j+1], st[j]
k=0

for i in range(10):
    for j in range(6):
        arr[i][j]=st[k]
        k=k+1
print('Posle sortirovki')

for i in range(10):
    for j in range(6):
        print(arr[i][j],end=" ")
    print()
