print("numbers: \n")
print("int(3.3) + 5//3:", int(3.3) + 5//3)
print("int(2) + 5%3 + 4.0:", int(2) + 5%3 + 4.0)
print("round(2.7, 0) + 3**2:", round(2.7, 0) + 3**2)
print('\n\n')
print("str: \n")
s1 = "lazy" 
s2 = "science"
print(s2[3]+s1[1]+s2[0]+s1[-1])
print("('EZ4.0'.find('.')*'EZ4.0'.replace('4.0','!')).lower():", ('EZ4.0'.find('.')*'EZ4.0'.replace('4.0','!')).lower())
def select_characters(s1,s2,selection):
    res = ''
    i = 0
    while i < len(selection):
        if selection[i] == '1':
            res += s1[i]
        else:
            res += s2[i]
        i += 1
    return res
print(select_characters('coat', 'hard', '1221'))
print('\n\n')
print('bool: \n')
print('(1>0) and ((2<3) or (5>=5))',((1>0) and ((2<3) or (5>=5))))
print('\n\n')
print('vars:\n')
x = 4
y = x + 5
x = 7
print(x, y)
print('\n\n')
print('functions:\n')
def f1(x,y):
    print("f1:", x, y)
    return x + y

def f2(x,y):
    print("f2:", x, y)
    return x * y

print("f1(f2(6,5),f1(2,4)):",f1(f2(6,5),f1(2,4)))
def square(x): 
    print('Squaring', x)
    return x * x 
def add(y, z): 
    print('Adding', y, z) 
    return y + z 

if add(-25, square(5)) > 0 and add(-4, square(10)) > 0: 
    print('Woohoo!') 
else: 
    print('Rats', add(square(3), 0))
print('\n')
def add(x, y): 
    print("ADD: " + str(x) + " + " + str(y)) 
    return x + y 
def multiply(x, y): 
    print("MULT: " + str(y) + " * " + str(x)) 
    return x * y 
def mystery_1(x, y): 
    x = x + y 
    y = y + x 
    print("Mystery 1: " + str(x) + " , " + str(y)) 
    return y 
def mystery_2(x, y): 
    x = mystery_1(add(x,y), multiply(x,y)) 
    print("Mystery 2: " + str(x) + " , " + str(y)) 
    return x + y 
x = 1 
y = 2 
print("STEP 1: " + str(add(x,y))) 
print("STEP 2: " + str(multiply(x,y))) 
print("STEP 3: " + str(mystery_1(x, y))) 
print("STEP 4: " + str(mystery_2(x, y))) 
print("STEP 5: " + str(mystery_2(mystery_1(x, y), x)))
print('\n')
def my_func(input_list):
    input_list[1][2] = 99
    input_list[0] = 100
def my_func2(input_list):
    my_list = input_list[:]
    my_list[1][2] = 99
    my_list[0] = 100
    return my_list
def my_func3(input_list):
    input_list[1] = [1, [2, 3, 4], 5]
    my_func2(input_list[1])
    return input_list
x=7
print("STEP1:",x)
y=x
x=9
print("STEP2:",x,"-",y)
x=1
y = [1, 2, 3]
z = ['a','b','c']
print("STEP3:",y[x],"-",z[y[x]])
x=1
y = [1, 2, 3]
z = [y,x,y]
y = [4,5,6]
print("STEP4:",y,'-',z)
x = [1, [3, 2, 1], [1, 2]]
y = my_func(x)
print("STEP5:",x,"-",y)
x = [1, [3, 2, 1], [1, 2]]
y = my_func2(x)
print("STEP6:",x,"-",y)
x = [1, [3, 2, 1], [1, 2]]
y = my_func3(x)
z = my_func3(y)
print("STEP7:",x,"-",y)
x = [1, [3, 2, 1], [1, 2]]
y = my_func(my_func2(my_func3(x)))
print("STEP8:",x,"-",y)
print('\n\n')
print('selection:\n')
total = 0
first = 4
second = 0
if first > 5:
    if first == 4:
        first = 6
        total = total + 1
    else:
        total = total + 2
else:
    if first > 5:
        total = total + 1
print (total)
print('\n\n')
print('list:\n')
def my_function(x, y):
    x.append(5)
    y = y + [5]
    
x = [1, 2, 3]
x1 = x
x2 = x[:]

y = [1, 2, 3]
y1 = y
y2 = y[:]

my_function(x, y)


print (x, y, x1, x2, y1, y2)
print('\n\n')
print("while:\n")
s = 'CSC-A08 is Fun!' 
i = 0 
while ((i < len(s)) and (s[i].isalpha())): 
    print(s[i]) 
    i = i + 1
print('\n')
my_list = ["1", 1, "2", 2, "3", 3, "4", 4]
i = 0
res = ""
while (i < len(my_list) and (isinstance(my_list[i], str) or (int(my_list[i]) < 3))):
    res += str(my_list[i])
    print(res)
    i += 1
print('\nfor\n')

my_list = ['*','x','-','#']
count = 0
for i in my_list:
    for j in range(0,len(my_list)):
        if(j + count > 2):
            print(i, end='')
        else:
            print('+', end ='')
    print('')
    count += 1
print('\n')
my_string = "Welcome to EZ4.0!"
result = ""
for next_letter in my_string:
    if (next_letter.isalpha()):
        result += "X"
    elif (next_letter.isdigit()):
        result += "#"
    else:
        result += "!"
    if (next_letter in "AEIOU"):
        print("VOWEL")
    if (next_letter in "Easy"):
        print("Take it easy")
print(result)
print('\n\n')
print('dict:\n')
my_text = "I-loved-CSCA08"
my_dict = {}

for i in range(0,len(my_text)-1):
    my_dict[my_text[i]] = my_text[i + 1]
    
for letter in my_dict:
    print(letter, " - ", my_dict[letter])

print('\n\n')
print('class:\n')
class CoolClass():
    def __init__(self, a, b):
        self._a = a
        self._b = b
    def __str__(self):
        return "Cool:" + self._a +"-"+ self._b
    def set_ab(self, a, b):
        self._a = a
        self._b = b
    def get_vals(self):
        return [self._a, self._b]
    
class BoringClass(CoolClass):
    def __init__(self, a, b, c):
        CoolClass.__init__(self, a, b)
        self._c = c
    def __str__(self):
        ret = CoolClass.__str__(self)
        ret += "-" + self._c
        return ret
    def get_vals(self):
        return [self._a, self._b, self._c]
    
class CrazyClass(BoringClass):
    def __init__(self, a, b, c):
        CoolClass.__init__(self, c, a)
        self._d = b
        self._c = BoringClass(c, b, a).get_vals()
    def __str__(self):
        return "CRAZY:" + str(self.get_vals())
    
if(__name__ == "__main__"):
    v1 = CoolClass('A', 'B')
    print(v1)
    v2 = BoringClass('A', 'B', 'C')
    print(v2)
    v2.set_ab('D', 'E')
    print(v2)
    v3 = CrazyClass('A', 'B', 'C')
    print(v3)
    v3.set_ab('A', 'B')
    print(CoolClass.get_vals(v3))
