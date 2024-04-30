# # Task 1

def get_int ():
    user_input = input("Write integer:")
    print(converted(user_input))
    get_int()

        
def converted(value):
    try:
        int_value = int(value)
        print("All is good")
        return int_value
    except ValueError:
        print("You should write integer")
        return get_int()
        
print(get_int())  

# # Task 2 

def get_input():
    int_input = input("Write an integer: ")
    string_input = input("Write a string: ")
    
    print_character_at_index(string_input,int_input)
    get_input()
        
def print_character_at_index(string, index):
    try:
        character = string[int(index)]
        print(f"The character at index {index} is '{character}'.")
    except IndexError:
        print(f"Index {index} is out of range for the string '{string}'.")
        get_input()
        
get_input()
        
# # Task 3

balance = 1000

def transaction(amount, the_type):
    if 'deposit' == the_type:
        deposit(amount)
    elif 'withdrawal' == the_type:
        withdrawal(amount)

    print('Current balance is: ' + str(balance))

def deposit(amount):
    global balance
    balance += amount

def withdrawal(amount):
    global balance
    balance -= amount

transaction(100, 'deposit')
transaction(100, 'withdrawal')


# # Task 4

import random

random.randint(1,6)

for i in range(6):
    print(random.randint(1,6))
        
        
# Task 5

import random

def roll_dice():
    return random.randint(1, 6)

def simulate_dice_rolls(num_rolls):
    rolls = []
    for _ in range(num_rolls):
        rolls.append(roll_dice())
    return count_rolls(rolls)

def count_rolls(rolls):
    roll_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for roll in rolls:
        roll_counts[roll] += 1
    return roll_counts

print(simulate_dice_rolls(1000))

def main():
    num_rolls = 1000
    rolls = simulate_dice_rolls(num_rolls)
    roll_counts = count_rolls(rolls)
    print("Results of rolling the dice", num_rolls, "rolles:")
    for number, count in roll_counts.items():
        print(f"Number {number} dropped {count} times.")
        

if __name__ == "__main__":
    main()

# Task 6

import random
from random import choices

def receive_input():
    number_of_regions = int(input('Enter the number of regions: '))
    list_of_regions = []
    for i in range(number_of_regions):
        list_of_regions.append(float(input("Enter a rating for 1st candidate in " + str(i + 1) + " region: ")))

    return list_of_regions

def simulate_elections(regions):
    result = []
    for rating in regions:
        result.append(simulate_region_election(rating))

    return result

def simulate_region_election(rating): 
    region_result = [0, 0]
    for candidate_index in random.choices([0, 1], [rating, 100 - rating], k=10000):
        region_result[candidate_index] += 1

    return region_result

def calculate_result(election_results):
    total_votes = [0, 0]
    for result in election_results:
        print("Region " + str(election_results.index(result) + 1) + " : " + str(result[0])  + " votes for 1st candidate, " + str(result[1]) + " votes for 2nd candidate")
        total_votes[0] += result[0]
        total_votes[1] += result[1]

    return total_votes

def anounce_result(votes):
    election_visitors = votes[0] + votes[1]
    winner_candidate_index = 0 if votes[0] > votes[1] else 1
    winner_abbreviation = "1st" if 0 == winner_candidate_index else "2nd"
    winner_rating = (votes[winner_candidate_index] / election_visitors) * 100

    print("Result: " + winner_abbreviation + " candidate won with " + str(votes[winner_candidate_index]) + " votes and " + str(winner_rating) + "% of all votes")

input_data = receive_input()
election_result = simulate_elections(input_data)
result = calculate_result(election_result)
anounce_result(result)