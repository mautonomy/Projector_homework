#Task 1

def triangle_area (x1, y1, x2, y2, x3, y3) :
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

print(triangle_area)

#Task 2
import re
s1 = "Гаррі Поттер (англ. Harry Potter) — серія з семи фантастичних романів англійської письменниці..."

print ("The original string is : " + s1)

result = len(re.findall(r'\w+', s1))

print ("The number of words in string are : " + str(result))


# # #Task 3 snake_case to CamelCase convertor
start_string = "snake_case_text"
splitted_sentence = start_string.split("_")
big_letters = [word.capitalize() for word in splitted_sentence]
end_string = ''.join(big_letters)
print(end_string)

# #Task 4 CamelCase to snake_case convertor

import re
 
s1 = "SnakeCaseText"
words = re.findall('[A-Z][a-z]*', s1)

for i in range(len(words)):
    print(words[i])
    words[i] = words[i].lower()
    print(words[i])

result = "_".join(words)

print(result)

# #Task 5

def anagram(s1, s2):
    return sorted(s1) == sorted(s2) 
        
s1 = "listen"
s2 = "silent"
print(anagram(s1, s2))



# Task 6 Fizz Buzz

def FizzBuzz(n):
    for i in range(n):
        index = i + 1
        print(index)
        if index % 15 == 0:
            print('fizz_buzz')
        elif index % 3 == 0:
            print('fizz')
        elif index % 5 == 0:
            print('buzz')

a = int(input())
FizzBuzz(a)


   