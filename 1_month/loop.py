# Task 1
# (False == not True)
# (True and False) == (True and False)
# (not True and) ("A" == "B")

# Task 2

def calculate_wheat_weight():
     total_grains = 2**64 - 1  
     weight_per_grain = 0.065  
     total_weight_grams = total_grains * weight_per_grain
     total_weight_tons = total_weight_grams / 1000000  
     return total_weight_tons


total_weight_tons = calculate_wheat_weight()

print("Total weight :", total_weight_tons, "tons")

#Task 3

def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = 6

print_factors(num)

# Task 4

def checkTriangle(x, y, z):
     if x == y == z:
         print("Equilateral Triangle")
     elif x == y or y == z or z == x:
         print("Isosceles Triangle")
     else:
         print("Scalene Triangle")
        
         
print("X:")        
x = int(input())
print("Y:")
y = int(input())
print("Z:")
z = int(input())
print(checkTriangle(x,y,z))

#Task 4

def longest_consecutive_symbol(s):
    max_symbol = '' 
    max_count = 0 
    current_symbol = ''  
    current_count = 0  

    for char in s:
        if char == current_symbol:
            current_count += 1 
        else:
            if current_count > max_count:
                max_count = current_count  
                max_symbol = current_symbol  
            current_symbol = char 
            current_count = 1 

    if current_count > max_count:
        max_count = current_count
        max_symbol = current_symbol

    return max_symbol

input_string = 'ommmmnomnomnomomom'
longest_symbol = longest_consecutive_symbol(input_string)
print("Longest consecutive symbol:", longest_symbol)





