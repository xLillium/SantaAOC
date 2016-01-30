# Day One AoC : http://adventofcode.com/day/1
directions = input("What are the directions for Santa?")
floor = 0
characterNb = 0
firstBasement = 0
firstCheck = True

for character in directions:
    characterNb += + 1
    if character == "(":
        floor +=  1
    elif character == ")":
        floor -=  1
    if firstCheck == True and floor == -1:
        firstCheck = False
        firstBasement = characterNb
if firstCheck == True:
    print("Santa ended up at floor : ", floor," but he never reached the basement")
else:
    print("Santa ended up at the floor: ", floor, ", the first character that made Santa enter the basement was the # : ",firstBasement)
