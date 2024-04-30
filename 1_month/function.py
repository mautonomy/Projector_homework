# # Task 1

def isPrimeNumber (number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def find_primes(a, b):
    for number in range(a, b + 1):
        if isPrimeNumber(number):
            print(number)
        
a = 3
b = 30
find_primes(a,b)

    
# Task 2

def unique_characters(s):
    temp_string = ""
    for element in s:
        if element in temp_string:
            return False
        temp_string = temp_string + element
    return True

s = "abcdeff"
print(unique_characters(s))

# Task 3

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    
    return fibonacci(n-1) + fibonacci (n-2)

print(fibonacci(10))

# Task 4

input_str = "HelLo!"
output_str=""
for char in input_str:
    if(char.isupper()):
        output_str+=char.lower()
    else:
        output_str+=char.upper()
print(output_str)

# Task 5

def simple_interest(initial_amount, interest_rate, years):
    final_amount = initial_amount
    for _ in range(years):
        final_amount += final_amount * interest_rate
        return round(final_amount)
        
print(simple_interest(10000, 0.1, 10))

# Task 6

def password_strength(password):
    score = 0
    lowercase_letters = set()
    uppercase_letters = set()
    digits = set()
    special_chars = set()
    for char in password:
        score += 1
        if char.islower():
            lowercase_letters.add(char)
            score += 2
        elif char.isupper():
            uppercase_letters.add(char)
            score += 3
        elif char.isdigit():
            digits.add(char)
            score += 4
        else :
            special_chars.add(char)
            score += 5
            
    score += len(lowercase_letters) * 2
    score += len(uppercase_letters) * 3
    score += len(digits) * 4
    score += len(special_chars) * 5

    return score
print(password_strength('abc123'))

# Task 7



        

