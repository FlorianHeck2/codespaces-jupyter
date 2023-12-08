S = input("What's your operation? (+ - * /) ")
n1 = input("Enter a Number ")
n2 = input("Enter another Number ")
if S == "+":
    res = int(n1) + int(n2)
    print(n1 + S + n2+" = " + str(res))
elif S == "-":
    res = int(n1) - int(n2)
    print(n1 + S + n2+" = " + str(res))
elif S == "*":
    res = int(n1) * int(n2)
    print(n1 + S + n2+" = " + str(res))
elif S == "/":
    res = int(n1) / int(n2)
    print(n1 + S + n2+" = " + str(res))
else:
    print("You didn't enter a valid operator. Try again!")

