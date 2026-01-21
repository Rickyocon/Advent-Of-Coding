#--------------------------------------------------

PuzzelInput = "2025\Day 2\Challenge 1\PuzzelInput.txt"

def FileToList(PathToInputFile):
    with open(PathToInputFile, 'r') as File:
        line = File.read().strip()
        list = line.split(',')
    return list

ListOfInput = FileToList(PuzzelInput)

#-------------------------------------------------- 

def IsPatternNumber(string):
    #Split string ing half and store each half to be compared
    FirstHalf = string[:len(string)//2] # take length of string and then split it in half -> colon in front means get eveything from the begining until the half
    SecondHalf =  string[len(string)//2:] # take length of string and then split it in half -> colon at end means get eveything from the half until the end
    if FirstHalf == SecondHalf:
        return True
    else:
        return False
    
#--------------------------------------------------

def GetRange(string):
    #Strings in the list are ranges of numbers which look something like this 11-35 for example so need to split into the two min and max and then convert to int and then get all numbers in between
    bounds = string.split("-")
    min = bounds[0]
    max = bounds[1]
    
    minNum = int(min)
    maxNum = int(max)

    ListOfNumbersInRange = list(range(minNum,maxNum+1))

#--------------------------------------------------

