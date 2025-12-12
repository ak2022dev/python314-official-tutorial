print("range(5) results in")
for i in range(5):
    print(i, end=' ')
print()

print("list(range(5,10)) results in:")
print(list(range(5, 10)))

print("list(range(0,10,3)) results in:")
print(list(range(0,10,3)))

print("list(range(-10,-100,-30)) results in:")
print(list(range(-10, -100, -30)))

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

