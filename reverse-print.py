lst = []

while True:
    n = int(input())
    if n != 0:
        lst.append(n)
    else:
        break

for i in lst[::-1]:
    print(i)