def gcd(num1, num2):
    while num2 !=0:
        num1, num2 = num2, num1%num2
    return num1

def iscoprime(n):
    for num1 in range(1,n):
        for num2 in range(num1+1,n):
            if gcd(num1, num2) == 1:
                print(f'(',num1,',',num2,')')

n = 5

iscoprime(n)