# 1 task

import random

def generate_files():
    summary = []
    for char in range (65,91):
        file_name = chr(char) + ".txt"
        random_number = random.randint(1, 100)
        with open(file_name, 'a') as file:
            file.write(str(random_number))
        summary.append(f"{file_name}: {random_number}\n")
    with open("summary.txt", 'w') as summary_file:
        summary_file.writelines(summary)
        
        

generate_files()
