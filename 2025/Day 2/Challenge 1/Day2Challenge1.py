#--------------------------------------------------

PuzzelInput = "Day 2\Challenge 1\PuzzelInput.txt"

def FileToList(PathToInputFile):
    with open(PathToInputFile, 'r') as File:
        line = File.read().strip()
        list = line.split(',')
    return list

ListOfInput = FileToList(PuzzelInput)

print(ListOfInput)

#-------------------------------------------------- 

def IsPatternNumber(string):
    #Split string ing half and store each half to be compared
    FirstHalf = string[:len(string)//2] # take length of string and then split it in half -> colon in front means get eveything from the begining until the half
    SecondHalf =  string[len(string)//2:] # take length of string and then split it in half -> colon at end means get eveything from the half until the end

    