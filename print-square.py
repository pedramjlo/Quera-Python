n = int(input())

space = " "

print("*" * n)
for i in range(n-2):
    print(f"*{space * (n-2)}*")
print("*" * n)

url_to_question = "https://quera.org/problemset/591"