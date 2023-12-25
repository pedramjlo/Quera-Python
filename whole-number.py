n = int(input())
lst = []

for i in range(1, n+1//2):
    if n % i == 0:
        lst.append(i)

print("YES" if sum(lst) == n else "NO")