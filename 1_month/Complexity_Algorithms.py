def change_hats(interval):
    for i in range(len(cats)):
        if (i + 1) % interval == 0:
            cats[i] = not cats[i]

cats = [False] * 100
for round in range(100):
    interval = round + 1
    change_hats(interval)

print('Cats which has hats: ')
for index, cat in enumerate(cats):
    if cat:
        print(index + 1)
