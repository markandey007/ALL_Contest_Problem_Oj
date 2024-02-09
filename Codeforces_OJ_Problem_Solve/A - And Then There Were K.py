for _ in range(int(input())):
    n = int(input())
    while n != 0:
        v = n-1
        if (n := n & (n-1)) == 0:
            print(v)
            break
