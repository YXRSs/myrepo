def f1(x, y):
    c = x[:]
    x[0] = 99
    print(c, x, y)
    return x
def f2(x, y):
    c = x[:]
    (c[0], c[y]) = (c[y], c[0])
    print(c, x, y)
    (x[0], c[y]) = (c[0], x[y])
    return c[x[y]]
def f3(x, y, z):
    x[y][z] = x[z][y]
    c = x[:]
    c[0][0] = f1(c[0], c[1][2])
    print(c[1:])
    x[1][1] = f1(c[0], c[1][2])
a = [1, 2, 3, 4, 5]
b = 2
print("STEP 1")
print(f1(a, b))
a = [[6, 5], [[4, 3], 2], 1]
b = 2
print("STEP 2")
print(f2(a, b))
print(a)
a = [[8, 7], [6, [5], 4], [[3, 2], 1]]
b = 1
c = 2
print("STEP 3")
print(f3(a, b, c))
print(a)
print (111111111111111111111111111111111111111111111111111)
string1 = "ABCDE"
string2 = "12345"
for i in range(len(string1) - 1, -1, -1):
    count = 0
    res = ""
    while(count < len(string2)):
        if(i < count):
            res += string1[i]
        elif(i == count):
            res += "X"
        else:
            res += string2[count]
        count += 1
    print(res)
print(111111111111111111111111111111111111111)
s1 = "CSCA08 2015"
s2 = "INTRO TO COMPUTER SCIENCE"
d1 = {}
d2 = {}
i = 0
j = len(s2) - 1
while(i < j):
    d1[s1[i]] = s2[j]
    if(s1[i] in s2):
        d2[i] = s2[j-i]
    i += 1
    j -= i
print(d1)
print(d2)
print(1111111111111111111111111111111111111111111)
def get_domain(input_email):
    '''(str) -> str
    Return the domain (the portion of the address between the @ symbol
    and the last period) in the e-mail address. If input_email is not
    a valid e-mail address, containing 1 @ symbol, and
    at least 1 . to the right of the @ symbol, return 'INVALID'
    >>> get_domain('brian.harrington@utsc.utoronto.ca')
    'utsc.utoronto'
    >>> get_domain('code@mangler.net')
    'mangler'
    >>> get_domain('brian@brian@harrington.com')
    'INVALID'
    >>> get_domain('brian.harrington@utscutorontoca')
    'INVALID'
    '''
    found_at = False
    found_second_at = False
    found_period = False    
    index = 0
    while(index < len(input_email) and not (found_at)):
        if(input_email[index] == '@'):
            found_at = True
            at_index = index
        index += 1   
    while(index < len(input_email) and not (found_second_at)):
        if(input_email[index] == '@'):
            found_second_at = True
        elif(input_email[index] == '.'):
            found_period = True            
            period_index = index
        index += 1   
    if(found_second_at or not(found_period)):
        result = "INVALID"
    else:
        result = input_email[at_index+1:period_index]
    return result
        
    
    

