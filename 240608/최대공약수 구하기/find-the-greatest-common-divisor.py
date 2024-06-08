n, m = input().split()

n = int(n)
m = int(m)

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

print(gcd(n, m))