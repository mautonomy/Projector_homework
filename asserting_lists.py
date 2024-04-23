# # Task 1

def get_difference(data: list, substract) -> list:
    result = data.copy()
    for element in substract:
        if element in result:
            result.remove(element)

    return result

def compute_difference(first: list, second: list) -> tuple:
    first_second = get_difference(first, second)
    second_first = get_difference(second, first)

    return first_second, second_first

def test_compute_difference():
    result1 = compute_difference(['a', 'b', 'c', 'c', 'd'], ['c', 'd', 'e'])
    assert result1 == (['a', 'b', 'c'], ['e'])

    result2 = compute_difference([], ['c', 'd', 'e'])
    assert result2 == ([], ['c', 'd', 'e'])

    result3 = compute_difference([1, 2, 3], [4, 4, 5, 6])
    assert result3 == ([1, 2, 3], [4, 4, 5, 6])

    result4 = compute_difference([1, 2, 3], [2, 3, 4])
    assert result4 == ([1], [4])


test_compute_difference()
print("All tests passed!")
    
    
# Task 2

def sum_of_two(nums: list, target: int) -> list:
    for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

print(sum_of_two([2,3,7,9,11],10))

def test_sum_of_two():
    result1 = sum_of_two([2,7,11,15], 9)
    assert result1 == [0, 1]
    result2 = sum_of_two([3,2,4], 6)
    assert result2 == [1, 2]
    result3 = sum_of_two([3,3], 6)
    assert result3 == [0, 1]

test_sum_of_two()
print("All tests passed!")

# Task 3


def unique_elements(arr: list) -> list:
    x = []
    for a in arr:
        if a not in x and arr.count(a) < 2:
            x.append(a)
    return x

def test_unique_elements():
    result1 = unique_elements([1, 2, 3, 2, 4, 5, 5])
    assert result1 == [1, 3, 4]
    result2 = unique_elements([1, 2, 3, 4, 5])
    assert result2 == [1, 2, 3, 4, 5]
    result3 = unique_elements([1, 1, 1, 1, 1])
    assert result3 == []
    
test_unique_elements()
print("All tests passed")

# Task 4

def odd_elements(arr: list) -> list:
    x = []
    for a in arr:
        if a not in x and arr.count(a) % 2 != 0:
            x.append(a)
    return x
    
def test_odd_elements():
    result1 = odd_elements([1, 2, 3, 2, 4, 5, 5])
    assert result1 == [1, 3, 4]
    result1 = odd_elements([1, 2, 3, 2, 4, 5, 5, 6, 6, 6])
    assert result1 == [1, 3, 4, 6]

    
test_odd_elements()
print("All tests passed")

# Task 5

def second_largest_element(arr: list) -> int:
    if len(arr) < 2:
        return None

    secondLargest = 0
    largest = max(arr)
    
    for i in arr:
        if i > largest:
            secondLargest = largest
            largest = i
        else:
            secondLargest = max(secondLargest, i)
    return secondLargest

input_list = [1, 2, 3, 2, 4, 5, 5]
print(second_largest_element(input_list))

def test_second_largest_element():

    result1 = second_largest_element([1, 2, 3, 2, 4, 5, 5])
    assert result1 == 5
    result2 = second_largest_element([1, 2, 3, 4, 5])
    assert result2 == 4
    result3 = second_largest_element([1, 1, 1, 1, 1])
    assert result3 == None
    
test_second_largest_element



def second_largest_element(arr):
  list = [x for x in arr if x < max(arr)]
  return max(list)
 
arr = [10, 20, 4, 45, 99]
print(second_largest_element(arr))

# Task 6

cities = [

    ('New York City', 8550405),

    ('Los Angeles', 3792621),

    ('Chicago', 2695598),

    ('Houston', 2100263),

    ('Philadelphia', 1526006),

    ('Phoenix', 1445632),

    ('San Antonio', 1327407),

    ('San Diego', 1307402),

    ('Dallas', 1197816),

    ('San Jose', 945942),

]

def sort_cities(cities: list) -> list:
    cities.sort(key=lambda city: city[1])
    return cities

print(sort_cities(cities))

