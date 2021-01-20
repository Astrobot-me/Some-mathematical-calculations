num = int(input("Enter your Number--"))
prime = True
for x in range(2,num):
   if(num%x == 0):
       prime = False
       pass
   
if prime:
    print(str(num) + "is a prime Number")
else:
    print(str(num) + " is not a prime")

    #another way
    """n = int(input("Enter number "))
c = 0
for x in range(2, int(n / 2)):
    if n % x == 0:
        c = 1
if c == 1:
    print(f"{str(n)} is a prime number")
else:
    print(f"{str(n)} is not a prime number")"""