x = int(input("Enter The year in format eg-2020--"))
if(x%100 == 0):
    if(x%400 == 0):
        print(str(x) +' is a leap year')
    else:
        print(str(x) +' is not a leap year')
else:
    if(x%4 == 0):
        print(str(x) +" is a Leap Year")
    else:
        print(str(x) +" is not a Leap year")
   