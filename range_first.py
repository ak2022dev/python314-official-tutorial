print("range(5) results in:")
for i in range(5):
    print(i, end=' ')
print()

print("list(range(5,10)) results in:")
print(list(range(5, 10)))

print("list(range(0,10,3)) results in:")
print(list(range(0,10,3)))

print("list(range(-10,-100,-30)) results in:")
print(list(range(-10, -100, -30)))

print("With list a = ['Mary', 'had', 'a', 'little', 'lamb'] printing i, a[i] with range(len(a)) results in:")
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print("sum(range(4)) results in:")
print(sum(range(4)))

