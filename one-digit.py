n = int(input())



while n > 9:
    n = sum(int(d) for d in str(n))


print(n)