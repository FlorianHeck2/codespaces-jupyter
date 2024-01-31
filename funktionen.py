fibonacci_cache = []
defaultdict = __import__('collections').defaultdict
count = defaultdict(int)
amount = 0
def fibonacci_of(n):
    global amount
    amount += 1
    if len(fibonacci_cache) > n:
        return fibonacci_cache[n]
    
    else:
        if n == 0:
            fibonacci_cache.append(0)
            return 0
        elif n == 1:
            fibonacci_cache.append(1)
            return 1
        elif n > 1:
            a = fibonacci_of(n-2) + fibonacci_of (n-1)
            fibonacci_cache.append(a)
            return a

n=1995

print(fibonacci_of(n))
# while n >= 0:
#     print(count[n])
#     n -= 1
    
print(amount)