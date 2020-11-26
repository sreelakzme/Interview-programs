#string palindrome
'''while True:
    str = input("Enter a string: ")
    rev = str[::-1]
    if rev == str:
        print("Palindrome")
    else:
        print("Not Palindrome")
    if str == "exit()":
        break
'''

#number palindrome

num = int(input("Enter any number: "))
temp = num
rev = 0

while(num > 0):
    a = num%10
    rev = rev *10 + a
    num = num//10

if (rev == temp):
    print("Palindrome")
else:
    print("Not Palindrome")


















