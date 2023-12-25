lst = []

for i in range(1, 4):
    n = int(input())
    lst.append(n)

lst.sort()

if ((max(lst)**2) == (lst[0]**2) + (lst[1]**2)):
    print("YES")
else:
    print("NO")