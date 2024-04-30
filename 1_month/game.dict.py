# # Task 1

import random
import sys

capitals = {
        'Ukraine': 'Kyiv', 'France': 'Paris', 'Germany': 'Berlin',
        'Italy': 'Rome', 'USA': 'Washington', 'Canada': 'Ottawa',
        'Switzerland': 'Bern', 'Austria': 'Vienna',
        'Belgium': 'Brussels',  'Sweden': 'Stockholm',
        'Norway': 'Oslo', 'Denmark': 'Copenhagen',
        'Finland': 'Helsinki', 'Poland': 'Warsaw',
        'Romania': 'Bucharest', 'Bulgaria': 'Sofia', 'Greece': 'Athens',
}

def get_random_country():
        country = random.choice(list(capitals.keys()))
        capital = capitals[country]
        return country, capital

def play_guessing_game():
    print("Welcome to the Game!")
    print("You will be given a country, and you have to guess its capital.")
    print("Type 'exit' at any time to quit the game.")

    score = 0
    while True:
        country, correct_capital = get_random_country()
        print(f"Country: {country}")
        guess = input("Guess the capital: ")
        
        if guess.lower() == 'exit':
                print("Bye, your score is" + score)
                break

        if guess.lower() == correct_capital.lower():
                score += 1
                print("You're right!")
        
        else:
                print("Try again")
        
        print(f"Your current score is: {score}")
        print(f"Your final score is: {score}")
    print("Thanks for playing!")
    

play_guessing_game()

        
# Task 4 majority element

def majority_element(nums: list) -> int:
        counts = {}
    
        for num in nums:
                if num in counts:
                        counts[num] += 1
                else:
                        counts[num] = 1
        majority_count = max(counts.values())
        for num, count in counts.items():
                if count == majority_count:
                        return num


nums = [2,2,1,1,1,2,2]
print("Output for nums:", majority_element(nums))

def test_majority_element():
        result1 = majority_element([3, 2, 3])
        assert result1 == 3

        result1 = majority_element([2, 2, 1, 1, 1, 2, 2])
        assert result1 == 2
        
test_majority_element()


# Task 5

def get_list_by_key(data: dict, key: str) -> list:
        result = []
        
        if key in data.keys():
                result = data[key]
        else:
                data[key] = result
                
        return result

def get_subjects_not_passed_by_all_students(student_exams):
        processed_exams = {}
        for exam in student_exams:
                get_list_by_key(processed_exams, exam[2]).append(exam[1])

        problematic_subjects = set()
        for subject in processed_exams.keys():
                if min(processed_exams[subject]) <= 60:
                        problematic_subjects.add(subject)
                        
        return problematic_subjects




def test_get_subjects_not_passed_by_all_students():
        exams = [
        ("Alice", 55, "Math"),
        ("Bob", 40, "Math"),
        ("Charlie", 30, "Math"),
        ("Alice", 50, "Science"),
        ("Bob", 45, "Science"),
        ("Charlie", 40, "Science"),
        ("Alice", 95, "History"),
        ("Bob", 85, "History"),
        ("Charlie", 90, "History")
        ]

        assert get_subjects_not_passed_by_all_students(exams) == {"Science", "Math"}

test_get_subjects_not_passed_by_all_students()
print("All tests passed")
        