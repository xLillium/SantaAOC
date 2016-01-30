# Day Four AoC : http://adventofcode.com/day/4
from hashlib import md5
secretKey = 'yzbqklnj'
zerosWanted = int(input("How many zeroes do you want your hash to start with?"))
wantedValue = "0"
for i in range(zerosWanted-1):
    wantedValue += "0"
for i in range(100000000):
    hashStart = md5((secretKey + str(i)).encode()).hexdigest()[:zerosWanted]
    if hashStart == wantedValue:
        print("The answer for a MD5 starting with ",zerosWanted, " zeros is :",i)
        break