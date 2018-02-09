def func1(x):
    print(x)
    x = 7
    return x
def func2(x, y):
    print(x + y)
    z = x
    x = y
    y = z
    print(str(x) + str(y))
    return x * y
def func3(x, y, z):
    print(func1(x))
    print(func1(func2(y, z)))
    z = func1(func1(x))
    return x + y + z
a = 3 * 3
b = 4.5 + 4.5
c = 9.0
print("--1--")
print(a, b, c)
print(str(a) + str(b) + str(c))
print(str(a + b + c))
print(a == b, a == c, a is b, a is c)
a = 1
b = 2
c = 3
print("--2--")
c = func1(b)
print(a, b, c)
a = func2(b, c)
print(a, b, c)
c = func2(c, c)
print(a, b, c)
x = 4
y = 5
z = 6
print("--3--")
r = func3(func1(x), func2(x, y), func2(func1(z), z))
print('000000000000000000000000000000000000000000000000000000000')
def concat(v1, v2):
    result = v1 + v2
    print("CONCAT: ", v1, v2, result)
    return result
def reverse(v1, v2):
    temp = v1
    v1 = v2
    v2 = temp
    print("REVERSE: ", v1, v2)
def splice(v1, v2):
    result = v1[0] + v2[0] + v1[1] + v2[1]
    print("SPLICE :", v1, v2, result)
    return result
def mystery(v1, v2):
    v1 = v1 + v2
    v2 = v2 + v1
    result = concat(v1, v2)
    print("MYSTERY 1:", v1, v2, result)
    result = reverse(v1, v2)
    print("MYSTERY 2:", v1, v2, result)
    result = splice(v1, v2)
    print("MYSTERY 3:", v1, v2, result)
    result = splice(v1, concat(v1, v2))
    return result
print("STEP 1:")
print(concat("A", "1"))
print("STEP 2:")
print(reverse("A", "1"))
print("STEP 3:")
print(splice("AB", "12"))
print("STEP 4:")
print(mystery("A", "1"))
print('000000000000000000000000000000000000000000000000000')
def func1(my_var1):
    my_var1 = "C"
    my_var1 = my_var1 + my_var1
    print(my_var1)
    return my_var1
def func2(my_var1, my_var2):
    my_var3 = func1(my_var1)
    my_var1 = my_var2 + my_var3
    print(my_var1,my_var2)
    return my_var3
def func3(my_var1, my_var2, my_var3):
    print(my_var1, my_var2, my_var3)
    my_var1 = func2(func2(my_var1, my_var2),func2(my_var2, func1(my_var3)))
    print(my_var1, my_var2, my_var3)
    return my_var1
my_var1 = "A"
my_var2 = 4
print("STEP 1:", my_var1, my_var2)
my_var1 = "A"
my_var2 = 4
my_var1 = func1(my_var2)
print("STEP 2:", my_var1, my_var2)
my_var1 = "A"
my_var2 = "B"
my_var3 = "C"
my_var3 = func2(my_var1, my_var2)
print("STEP 3:", my_var1, my_var2, my_var3)
my_var1 = "A"
my_var2 = "B"
my_var3 = "C"
my_var3 = func3(my_var1, my_var2, my_var3)
print("STEP 4:", my_var1, my_var2, my_var3)
print('000000000000000000000000000000000000000000000')
def func1(l1):
    l1[0] = "X"
    print(l1)
def func2(l1, l2):
    l1[0] = l2[0]
    l3 = l1[0:3]
    l3[0] = "Y"
    l2[0] = l3[0]
    print(l1, l2, l3)
def func3(l1, l2):
    l3 = l1[:]
    l1[0] = l2
    l1[0][0] = "Z"
    l2[1] = "W"
    print(l1, l2, l3)
l1 = [1, 2, 3]
l2 = [7, 8, 9]
func1(l1)
func2(l1,l2)
l1 = [1, 2, 3]
l2 = [7, 8, 9]
func3(l1, l2)
l1 = [[1, 2], 3]
l2 = [[7], [8, [9]]]
func3(l1, l2)
