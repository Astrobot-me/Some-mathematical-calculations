x = int(input('Enter the 1st Number:--'))
y = int(input('Enter the 2nd Number:--'))
m = max(x ,y)
if(x==0 or y==0):
    print(f'LCM of {x} and {y} is NOT defined')
else:
    while True:
        if(m%x==0 and m%y==0):
            break
        m=m+1
    print(f'Lcm of {x} and {y} is {m}')

