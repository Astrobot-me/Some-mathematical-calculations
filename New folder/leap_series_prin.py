
import time
z=""" using this you can able to print leap years in series"""
print(z)
time.sleep(4)
x = int(input("Enter The first year in the format eg-2020--"))
y = int(input("Enter The  last year in the format eg-2020--"))
for i in range(x,y+1):
    if(i%100 == 0):
        if(i%400 == 0):
            print(str(i) +' is a leap year') #use pass statement in if wanna print leap year only
        else:
            print(str(i) +' is not a leap year') 
    else:
        if(i%4 == 0):
            print(str(i) +" is a Leap Year")
        else:
            print(str(i) +' is not a leap year')#use pass statement in if wanna print leap year only

   
   