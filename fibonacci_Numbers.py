
import time

def recursive(n):
    if n <= 1:
        return n
    return recursive(n-1) + recursive(n-2)

def non_recursive(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a+b

n = int(input("Enter number of elements: "))

# Recursive
start = time.time()
for i in range(n):
    print(recursive(i), end=" ")
print("\nRecursive Time:", (time.time()-start)*1000000, "microseconds")

# Non-Recursive
start = time.time()
non_recursive(n)
print("\nNon-Recursive Time:", (time.time()-start)*1000000, "microseconds")

print("\nRecursive: Time O(2^n), Space O(n)")
print("Non-Recursive: Time O(n), Space O(1)")
