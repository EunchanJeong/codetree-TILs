a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

def func(a, b, c):
    min_num = min(a, b)
    min_num = min(min_num, c)

    return min_num

print(func(a, b, c))