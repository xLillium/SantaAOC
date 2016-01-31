# Day Five AoC : http://adventofcode.com/day/5
textFile = open("InputDay5").read().split()
badStrings = ['ab', 'cd', 'pq', 'xy']
vowels = ['a','e','i','o','u']
def part1():
    nbNiceText = 0
    for text in textFile:
        if any(i in text for i in badStrings):
            continue
        elif sum(text.count(i) for i in vowels) < 3:
            continue
        elif all(text[i] != text[i+1] for i in range(len(text)-1)):
            continue
        nbNiceText += 1
    print(nbNiceText)

def part2():
    nbNiceText = 0
    for text in textFile:
        if all((text[i] != text[i+2]) for i in range(len(text)-2) ):
            continue
        elif all( text.count(str(text[i]+text[i+1])) != 2 for i in range(len(text)-1) ):
            continue
        nbNiceText += 1
    print(nbNiceText)


menu = input("Do you wanna filter the texts by the old rules (Press 1 for Part 1) ? Or by the new ones (Press 2 for Part2) ? ")
if menu == "1":
    part1()
elif menu == "2":
    part2()