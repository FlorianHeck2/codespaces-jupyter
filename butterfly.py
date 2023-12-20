
max = 7
for x in range(2):
    for l in range (max-1):
        print(" ", end=" ")
    print("0", end = " ")
    for k in range(int(max/5)):
        print(" ", end = " ")
    print("0", end = " ")
    print()

for x in range(2):
    for l in range (max-1):
        print(" ", end=" ")
    for k in range(int(max/5)+2):
        print("0", end = " ")
    print()
    
for i in range(max):
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

for i in range(max):
    for j in range(max-i-1):
        print("0", end = " ")
    for m in range(i):
        print(" ", end = " ")
    for k in range(int(max/5)+2):
        print("0", end = " ")
    for n in range(i):
         print(" ", end = " ")
    for l in range(max-i-1):
         print("0", end=" ")
    print()

for x in range(2):
    for l in range (max-1):
        print(" ", end=" ")
    for k in range(int(max/5)+2):
        print("0", end = " ")
    print()

