a  = [1, 2, 3, 4]

def some_f(a, x):
    a = a[:]
    a.append(x)
    return a

b = some_f(a, 55)

print(b)
print(a)
print(a is b)
