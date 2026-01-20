#--- Day 1, challenge 2: Secret Entrance ---#

##BTW truned off these settings in VS Code to avoid auto fixing the code and suggestrions: Editor › Inline Suggest › Experimental: Empty Response Information & Editor › Inline Suggest: Enabled

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Global Variables
startingPosition = 50
currentPosition = startingPosition
ZeroPositionCounter = 0

#Open and read the input file
FilePath = "Day 1\Challenge 2\SafeInputNumbers.txt"

#function to read the input file and convert it to an array
def file_To_Array(RelativeFilePath):
    Arr = []
    with open(RelativeFilePath) as File:
        Arr = [line.strip() for line in File]
    return Arr

ArrayOfInstructions = file_To_Array(FilePath)

for instruction in ArrayOfInstructions:

    direction = instruction[0]  #this uses string indexing to grab the first character of the string for each element in the array of instructions ie L19 would take the L
    InstructionStringValue = instruction[1:] #this takes the remaing charactoers in the string of instrcuotns ie L19 would take the 19
    InstructionIntegerValue = int(InstructionStringValue)

    if direction == "L":
        #currentPosition = (currentPosition - InstructionIntegerValue + 100) % 100
        for i in range(InstructionIntegerValue):
            currentPosition = (currentPosition - 1 + 100) % 100
            if currentPosition == 0:
                ZeroPositionCounter += 1

    elif direction == "R":
        #currentPosition = (currentPosition + InstructionIntegerValue + 100) % 100
        for i in range(InstructionIntegerValue):
            currentPosition = (currentPosition + 1) % 100
            if currentPosition == 0:
                ZeroPositionCounter += 1
    else:
        print("Something went wrong, neither an L or R was provided")

print("The Passcode to the safe is:", ZeroPositionCounter)
