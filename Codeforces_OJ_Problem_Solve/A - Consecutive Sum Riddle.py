for _ in range(int(input())):
  if (n := int(input())) == 1:
    print(0,1)
  else:
    print("-"+str(n-1),n)
