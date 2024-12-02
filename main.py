# Version 1 used no function
# Version 2 moves the determination to a function

num_lines = 0
master_sum = 0

# Set up the parameters
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def determine_valid_pull(pull):
    """Determines if a bag pull is valid by checking that each group's colors
    do not exceed the maximums

    args:
    pull (String): a semi-colon separated list of cubes and color count

    :return:
    Returns True if the pull is valid and False if not
    """
    valid = True

    # for the game, divide the cubes
    cubes = pull.split(",")

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
                    valid = False
                    break
            case 'green':
                if int(count) > MAX_GREEN:
                    valid = False
                    break
            case 'red':
                if int(count) > MAX_RED:
                    valid = False
                    break

    # I think i need a break here to break out of the for loop
    if not valid:
        return False
    return True


# Open a document
doc = open('input.txt', 'rt')

for line in doc:
    # Read a line
    num_lines = num_lines + 1

    # set up the game
    valid_game = True

    # Determine the game ID and store it

    # Split the line into title and pulls
    temp = line.split(":")
    title = temp[0]
    tmp2 = temp[1]

    print(f"Game Title: {title}")
    temp = title.split(" ")
    game_id = int(temp[1])

    # Split the games
    pulls = tmp2.split(";")
    print('-----------------------')
    print(line)


    # Analyze each game and determine if it meets the criteria
    for pull in pulls:
        valid_game = determine_valid_pull(pull)
        # stop processing more pulls
        if not valid_game:
            break

    if valid_game:
        print(f"Game {game_id} is valid and should be added.")
        master_sum = master_sum + game_id
    else:
        print(f"Game {game_id} is NOT VALID")

# Close the document
doc.close()

# print the master number
print(f'The sum of the IDs of the games is {master_sum} based on {num_lines} lines')