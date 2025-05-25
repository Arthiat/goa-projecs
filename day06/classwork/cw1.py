num = int(input("input a numb: "))

for i in range (2, num+1):
    if num % i == 0:
        print("prime")
    else:
        print("not prime")