# Day Six AoC : http://adventofcode.com/day/6
import re
grid = [[0]*1000 for i in range(1000)]

def part1(grid):
    lightsOn = 0
    instructions = open("InputDay6")
    for instruction in instructions:
        lightsCoord = [int(s) for s in re.findall("\d+", instruction)]
        x = lightsCoord[2] - lightsCoord[0] + 1
        y = lightsCoord[3] - lightsCoord[1] + 1
        for i in range (x):
            for j in range (y):
                if "toggle" in instruction:
                    if grid[lightsCoord[0]+i][lightsCoord[1]+j] == 0:
                        grid[lightsCoord[0]+i][lightsCoord[1]+j] = 1
                    elif grid[lightsCoord[0]+i][lightsCoord[1]+j] == 1:
                        grid[lightsCoord[0]+i][lightsCoord[1]+j] = 0
                elif "on" in instruction:
                    grid[lightsCoord[0]+i][lightsCoord[1]+j] = 1
                elif "off" in instruction:
                    grid[lightsCoord[0]+i][lightsCoord[1]+j] = 0
    instructions.close()
    for i in range(1000):
        for j in range(1000):
            if grid[i][j] == 1:
                lightsOn += 1
    print("You have : ",lightsOn," lights on ! Wonderful !")

def part2(grid):
    brightness = 0
    instructions = open("InputDay6")
    for instruction in instructions:
        lightsCoord = [int(s) for s in re.findall("\d+", instruction)]
        x = lightsCoord[2] - lightsCoord[0] + 1
        y = lightsCoord[3] - lightsCoord[1] + 1
        for i in range (x):
            for j in range (y):
                if "toggle" in instruction:
                    grid[lightsCoord[0]+i][lightsCoord[1]+j] += 2
                elif "on" in instruction:
                    grid[lightsCoord[0]+i][lightsCoord[1]+j] += 1
                elif "off" in instruction:
                    if grid[lightsCoord[0]+i][lightsCoord[1]+j] > 0:
                        grid[lightsCoord[0]+i][lightsCoord[1]+j] -= 1
    instructions.close()
    for i in range(1000):
        for j in range(1000):
            brightness += grid[i][j]
    print("You have a total brightness of : ",brightness," ! Wonderful !")

menu = input("Press 1 for Part 1, or press 2 for Part 2 ")
if menu == "1":
    part1(grid)
elif menu == "2":
    part2(grid)