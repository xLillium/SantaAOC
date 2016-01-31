# Day Two AoC : http://adventofcode.com/day/2
paperNeeded = 0
ribbonNeeded = 0

boxList = open("InputDay2")
for box in boxList:
    boxDimensions = list(map(int,box.split("x")))
    l = boxDimensions[0]
    w = boxDimensions[1]
    h = boxDimensions[2]
    boxArea = 2*l*w + 2*w*h + 2*h*l
    boxDimensions.sort()
    slackArea = boxDimensions[0] * boxDimensions[1]
    ribbonArea = 2*boxDimensions[0] + 2*boxDimensions[1]
    bowArea = l * w * h
    paperNeeded += boxArea + slackArea
    ribbonNeeded += ribbonArea + bowArea
boxList.close()
print("The elves should order : ",paperNeeded," square feet of wrapping paper and ",ribbonNeeded," square feet of ribbon.")