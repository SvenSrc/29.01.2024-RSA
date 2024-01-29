import math

print("What is your message?")
m = int(input())

print()
# Setting the value for p and q
print("Enter a prime number 'p': ")
p = int(input())
isPrime = False

while(isPrime == False):
    if(p > 1):
        if(p == 2):
            isPrime = True
            break

        for i in range(2, math.ceil(p/2)+1):
            if(p % i) == 0:
                print(f"{p} is not a prime. Enter a another number")
                p = int(input())
                break
            else:
                isPrime = True
                break
    else:
        print(f"{p} is not a prime. Enter another number")
        p = int(input())


print("Enter a prime number 'q': ")
q = int(input())
isPrime = False

while(p == q):
    print("'p' and 'q' cannot be the same. Enter another number for q")
    q = int(input())

while(isPrime == False):
    while(p == q):
        print("'p' and 'q' cannot be the same. Enter another number for q")
        q = int(input())

    if(q == 2):
        isPrime = True
        break    

    if(q > 1):
        for i in range(2, math.ceil(q/2)+1):
            if(q % i) == 0:
                print(f"{q} is not a prime. Enter a another number")
                q = int(input())
                break
            else:
                isPrime = True
                break
    else:
        print(f"{q} is not a prime. Enter another number")
        q = int(input())

# Calculate RSA-Modul
n = p * q

# Calculating phi(n)
phin = (p - 1) * (q - 1)

print()
# Get a value for e
print("Enter a value for 'e' that is a prime and not the same as 'p' or 'q': ")
e = int(input())
isValid = False

while(e == p or e == q):
    print("'e' cannot be the same as 'p' or 'q'. Enter another number for q")
    e = int(input())

while(isValid == False):
    while(e == p or e == q):
        print("'e' cannot be the same as 'p' or 'q'. Enter another number for q")
        e = int(input())

    if(e > 1):
        if(e == 2 and e != p and e != p):
            isValid = True
            break

        for i in range(2, math.ceil(e/2)+1):
            if(e % i) == 0:
                print(f"{e} is not a prime. Enter another number")
                e = int(input())
                break
            else:
                if((math.gcd(phin, e)) == e or 1):
                    isValid = True
                else:
                    print("Enter another Number for 'e'")
                    e = int(input())
                break
    else:
        print(f"{e} is not a prime. Enter a another number")
        e = int(input())

print()
# Multiplicative Inverse for d
d = pow(e, -1, phin)

# Encrypt m
c = pow(m, e, n)

print(c)