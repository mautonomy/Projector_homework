# 1 task

# import random

# def generate_files():
#     summary = []
#     for char in range (65,91):
#         file_name = chr(char) + ".txt"
#         random_number = random.randint(1, 100)
#         with open(file_name, 'a') as file:
#             file.write(str(random_number))
#         summary.append(f"{file_name}: {random_number}\n")
#     with open("summary.txt", 'w') as summary_file:
#         summary_file.writelines(summary)
        
        

# generate_files()


# 2 task

# with open("file1.txt", "w") as file:
#     file.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum")

# with open("file1.txt", "r") as file1, open("file2.txt", "w") as file2:
#     content = file1.read()
#     file2.write(content.upper())
    
    

# 3 task

import random
import csv

def simulate_rounds():
    return sum([random.randint (1,15) for i in range(100)])

players = [ "Josh", "Luke", "Kate", "Mark", "Mary" ]

player_scores = [(player, simulate_rounds()) for player in players]

    
with open('players.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Player', 'Score'])
    for player, score in player_scores:
        writer.writerow([player, score])
        
        
# task 4

with open('players.csv', mode='r') as file:
    reader = csv.reader(file)
    for player, score in reader:
        print(player, score)