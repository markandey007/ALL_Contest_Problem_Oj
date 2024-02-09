a = str(input())
b = str(input())
c = str(input())
if (add := list(a+b+c)) == add[::-1]:
    print("YES")
else:
    print("NO")
