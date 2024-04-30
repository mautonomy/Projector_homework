# # 1 task
10 > 5
42 == "42"
3!=4

# # 2 task
line = 'He said: \"My name is Sherlock Holmes"'
print(line)


# # 3 task
string = input()
if string == string[::-1]:
    print("Yes")
else:
    print("No")

# 4 task
print("Type name")
name = input()
print("Type age")
age = input()
sentence = "My name is {} and I\'m {} years old"
print("name", name, "age", age)
print(sentence.format(name, age))
intro_string = f'My name is {name}, and I\'m {age} years old'
print(intro_string)

# 5 task

string_1 = "Animals  "
new_string1 = string_1.lower()
print(new_string1)


string_2 = " Badger"
new_string2 = string_2.upper()
print(new_string2)

# c) 
string_3 = "   HoneyPot   "
new_string_c = string_3.strip()
print(new_string_c)

# a)

new_string_a = string_3.lstrip()
print(new_string_a)

# b)
new_string_b = string_3.rstrip()
print(new_string_b)


#5 task
string_1 = "Bear"
string_2 = "bear"
string_3 = "BEAR"
string_4 = "bEar"


print(string_1.startswith('Be'))  
print(string_2.startswith('Be'))  
print(string_3.startswith('Be'))  
print(string_4.startswith('Be'))  

# 6task

string_1 = "Bear"
string_2 = "bear"
string_3 = "BEAR"
string_4 = "bEar"


upd_string_1 = string_1.capitalize()
upd_string2 = string_2.replace("b","B")
upd_string3 = string_3.lower().capitalize()
upd_string4 = string_4.title()


print(upd_string_1.startswith('Be'))  
print(upd_string2.startswith('Be')) 
print(upd_string3.startswith('Be')) 
print(upd_string4.startswith('Be')) 



