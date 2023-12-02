# Part 1 was to check if each game was possible
# we were given the max amount of red, green, blue cubes in the bag
# the task was to add ID numbers (game numbers)

import re

RED = 12
GREEN = 13
BLUE = 14

result_1 = 0

with open("data.txt") as my_file:
    for line in my_file:
        line =  line.strip()
        split_data = re.split('[:;,]', line)

        for idx, item in enumerate(split_data):
            game_cubes = item.split()

            if idx == 0:
                ID = int(game_cubes[1])

            if game_cubes[1] == 'red':
                if int(game_cubes[0]) > RED:
                    ID = 0
            elif game_cubes[1] == 'green':
                if int(game_cubes[0]) > GREEN:
                    ID = 0
            elif game_cubes[1] == 'blue':
                if int(game_cubes[0]) > BLUE:
                    ID = 0

        result_1 += ID

    print(f"Result Part 1: {result_1}")
