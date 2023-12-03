# Part 2 was to check the least amount of cubes possible
# for each game we have the fewest possible of red green, blue
# we then have to multiply RED * GREEN * BLUE to get this game's 'score' and add it to the result

import re

fewest = {'red': 0, 'green': 0, 'blue': 0}

result_2 = 0

with open("data.txt") as my_file:
    for line in my_file:
        line =  line.strip()
        split_data = re.split('[:;,]', line)
        
        # Apart from the first piece of data where Id is, the rest are organised as  number : colour
        for idx, item in enumerate(split_data):
            game_cubes = item.split()

            if idx == 0:
                ID = int(game_cubes[1])
                continue
            colour = game_cubes[1]
            number = int(game_cubes[0])

            if fewest[colour] < number : fewest[colour] = number

        ID = 0
        result_2 += (fewest['red'] * fewest['green'] * fewest['blue'])
        fewest = {'red': 0, 'green': 0, 'blue': 0}
    print(f"Part 2 result: {result_2}")