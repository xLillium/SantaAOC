# Day One AoC : http://adventofcode.com/day/1
directions = input("What are the directions for Santa?")
floor = 0
characterNb = 0
firstCheck = True


while floor >= 0:
    for character in directions:
        if character == "(":
            floor = floor + 1
        elif character == ")":
            floor = floor - 1
        if firstCheck == True:
            characterNb = characterNb + 1
            if floor < 0:
                firstCheck = False
    if firstCheck == True:
        print("Santa ended up at floor : ", floor," but he never reached the basement")
    else:
        print("Santa ended up at the floor: ", floor, ", the first character that made Santa enter the basement was the # : ",characterNb)
    break