for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    if a+c == 180 and b+d == 180:
        print("YES")
    else:
        print("NO")
