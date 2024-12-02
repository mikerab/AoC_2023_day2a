# Version 1 used no function
# Version 2 moves the determination to a function

num_lines = 0
master_sum = 0

# Set up the parameters
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

# Open a document
doc = open('input.txt', 'rt')

for line in doc:
    # Read a line
    num_lines = num_lines + 1

    # set up the game
    valid_game = True

    # Determine the game ID and store it
    id_split = line.split(":", 1)
    print(id_split[0])
    game_id = id_split[0]

    # Split the games
    games = id_split[1].split(";")
    print('-----------------------')
    print(line)


    # Analyze each game and determine if it meets the criteria
    for game in games:

        # for the game, divide the cubes
        cubes = game.split(",")

        # for each cube determine the color and the count
        for cube in cubes:
            cube = cube.strip()
            pair = cube.split(" ")
            color = pair[1]
            count = pair[0]
            # print(f"for color {color}, the count is {count}")

            # now compare the color's count against the max color value. If greater, the game is invalid
            match color:
                case 'blue':
                    if int(count) > MAX_BLUE:
                        valid_game = False
                        break
                case 'green':
                    if int(count) > MAX_GREEN:
                        valid_game = False
                        break
                case 'red':
                    if int(count) > MAX_RED:
                        valid_game = False
                        break

        # I think i need a break here to break out of the for loop
        if not valid_game:
            # print(f"Game {game_id} is not valid.")
            break

    game_id = game_id.split(" ")
    num_to_sum = int(game_id[1])

    if valid_game:
        print(f"Game {game_id} is valid and should be added.")
        master_sum = master_sum + num_to_sum
    else:
        print(f"Game {game_id} is NOT VALID")

        # If we got here, the set was valid




# Close the document
doc.close()

# print the master number
print(f'The sum of the IDs of the games is {master_sum} based on {num_lines} lines')