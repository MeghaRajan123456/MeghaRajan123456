a=int(input('enter number of pattern:'))
for i in range(1,a+1):
    for j in range(1, i+1):
        print(j%2, end="")
    print()