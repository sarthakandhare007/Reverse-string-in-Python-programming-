a = input("Enter a string: ")
a = list(a)   # convert string to list because strings are immutable

l = len(a)

for i in range(l // 2):   # loop only till half
    a[i], a[l - i - 1] = a[l - i - 1], a[i]   # swap directly

print("Reversed string is:", "".join(a))
