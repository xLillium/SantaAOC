# Day Two AoC : http://adventofcode.com/day/3
location = [0, 0]
locationList = {"0,0"}

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
    locationList.add(str(location[0]) + "," + str(location[1]))
print(len(locationList))
