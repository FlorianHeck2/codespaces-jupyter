max = 5
for i in range(max*2):
    for j in range(i):
        print("0", end = " ")
    for m in range(max-i-1):
        print(" ", end = " ")
    for k in range(int(max/5)+2):
        print("0", end = " ")
    for n in range(max-i-1):
         print(" ", end = " ")
    for l in range(i):
         print("0", end=" ")
    print()