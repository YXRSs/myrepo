def copy_me(li):
    res = []
    for i in li:
        if type(i) == str:
            res.append(i.upper())
        elif type(i) == int or type(i) == float:
            i = i + 1
            res.append(i)
        elif type(i) == bool:
            res.append(not i)
        elif type(i) == list:
            res.append("List")
    return res

def mutate_me(li):
    i = 0
    while i < len(li):
        if type(li[i]) == str:
            li[i] = li[i].upper()
        elif type(li[i]) == int or type(li[i]) == float:
            li[i] += 1
        elif type(li[i]) == bool:
            li[i] = not li[i]
        elif type(li[i]) == list:
            li[i] = 'List'
        i += 1
def pig_latin(input_string):
    if(input_string[0] in "aeiou"):
        result = input_string + "w"
    else:
        count = 1
        found_vowel = False
        while(count < len(input_string) and not found_vowel):
            if(input_string[count] in "aeiou"):
                found_vowel = True
                first_vowel_index = count
                result = input_string[first_vowel_index:] + input_string[0:first_vowel_index]
            else:
                count += 1
    result += "ay"
    return result
'''
if(__name__ == "__main__"):
    result = ""
    test_file = open("test_file.txt", "r")
    for next_line in test_file:
        next_line_words = next_line.split()
        for next_word in next_line_words:
            result += pig_latin(next_word) + " "
    print(result)
    test_file.close()
'''
print ("2015 tt2 1")
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
print ("2015 tt2 2")
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

print("\n2014 midterm 1")
my_list = ['A', 'B', 'C', 'D', 'E']
count = 0
while(count <5):
    res = ''
    for i in range(0,5):
        if(i >= count):
            res += my_list[count]
        else:
            res += '+'
    count += 1
    print(res)
print ("\n2014 midterm 2")
def f1(L):
    print(L[0])
    return L[-1]
def f2(L):
    L.insert(0, L[0] + L[1])
    L[1] = 2 * f1(L)
    print(L.pop())
    return (L[-1] + L[-2])
my_list = [2, 5]
print("STEP 1")
print(f1(my_list))
print(my_list)
my_list = [2, 5]
print("STEP 2")
print(f2(my_list))
print(my_list)
my_list = ["one", "two", "three", "four"]
print("STEP 3")
print(f1(my_list))
print(my_list)
my_list = ["one", "two", "three", "four"]
print("STEP 4")
print(f2(my_list))
print(my_list)
