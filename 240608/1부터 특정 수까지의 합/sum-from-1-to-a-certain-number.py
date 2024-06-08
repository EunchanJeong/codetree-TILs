def func(n):
    count = 0
    for i in range(1, n+1):
        count += i
    
    return count//10


n = int(input())

print(func(n))