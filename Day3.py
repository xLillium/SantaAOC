# Day Three AoC : http://adventofcode.com/day/3
# Part 1 :
def part1():
    location = [0, 0]
    locationSet = {"0,0"}

    directions = input("What are the directions for Santa?")
    for direction in directions:
        if direction == ">":
            location[0]+=1
        if direction == "<":
            location[0]-=1
        if direction == "^":
            location[1]+=1
        if direction == "v":
            location[1]-=1
        locationSet.add(str(location[0]) + "," + str(location[1]))
    print("Santa visited at least once : ",len(locationSet)," houses !")

# Part 2 :
def part2():
    santaLocation = [0,0]
    roboLocation = [0,0]
    locationSet = {"0,0"}
    turn = 0
    tempLocation = [0,0]

    directions = input("What are the directions for Santa?")
    for direction in directions:
        turn += 1
        if direction == ">":
            tempLocation[0]+=1
        if direction == "<":
            tempLocation[0]-=1
        if direction == "^":
            tempLocation[1]+=1
        if direction == "v":
            tempLocation[1]-=1
        locationSet.add(str(tempLocation[0]) + "," + str(tempLocation[1]))
        if turn % 2 == 1:
            santaLocation = tempLocation
            tempLocation = roboLocation
        elif turn % 2 == 0:
            roboLocation = tempLocation
            tempLocation = santaLocation
    print("Santa and Robo-Santa visited at least once : ",len(locationSet)," houses !")

menu = input("Is Santa alone (Part 1) ? Or is he with Robo-Santa (Part2) ? ")
if menu == "1":
    part1()
elif menu == "2":
    part2()