#fibonacci Series in python
a = 0
b = 1
c = 0
num = int(input("Enter how many numbers you want in series:"))
print("Fibonacci series: ",end=" ")
count = 1

while count <= num:
    print(c,end=" ")
    count += 1
    a = b
    b = c
    c = a + b
    
