def isprime(number):
    for i in range(2,number):
        if(number%i==0):
           return 0
    return (1)

if isprime(15):
    print ("prime")
else :
    print("not prime")

