def gcd(a,b):
    i = min(a,b)
    while True:
        if a % i ==0 and b % i ==0:
            return i
        i = i - 1

print(gcd(1,5))


# 유클리드 호재법
# a와b의 최대공약수는 b와 a를 b로 나눈나머지의 최대공약수와 같다
# gcd(60, 24) = gcd(24, 60%24) = gcd(24, 12) = gcd(12, 24%12) = gcd( 12, 0) = 12

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(1,5))
print(gcd(3,12))
print(gcd(60,24))


# 피보나치 수열
def fibo(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


print('fibo', fibo(8))
