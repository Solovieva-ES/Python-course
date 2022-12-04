n = int(input("Количество чисел, которые нужно суммировать: "))
summary = 0

for i in range(n):
    x = int(input())
    summary += x

print(summary)
