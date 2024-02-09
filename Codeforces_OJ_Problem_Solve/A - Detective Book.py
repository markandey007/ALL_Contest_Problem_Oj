n = int(input())
arr = list(map(int,input().split()))[:n]
day = 0
i = 0
m = 0
for j in arr:
    i += 1
    if (m := max(m,j)) == i:
        day += 1
print(day)
