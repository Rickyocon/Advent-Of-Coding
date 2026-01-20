#--- Day 1, challenge 1: Secret Entrance ---#

#only one arrow
#Numbers: 0-99
#L = Left, R= Right
#So, if the dial were pointing at 11, a rotation of R8 would cause the dial to point at 19. After that, a rotation of L19 would cause it to point at 0

#The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence (Meaning how many times the dial lands on 0
#for example if the note provides you with a sequence and while doing that sequence the dial lands on 0 three times, the password is 3)

##The dial starts by pointing at 50

##BTW truned off these settings in VS Code to avoid auto fixing the code and suggestrions: Editor › Inline Suggest › Experimental: Empty Response Information & Editor › Inline Suggest: Enabled

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Global Variables
startingPosition = 50
currentPosition = startingPosition
ZeroPositionCounter = 0

#Open and read the input file
File = "Day 1\Challenge 1\SafeInputNumbers.txt"

#function to read the input file and convert it to an array
def file_To_Array(RelativeFilePath):
    Arr = []
    with open(RelativeFilePath) as File:
        Arr = [line.strip() for line in File]
    return Arr

ArrayOfInstructions = file_To_Array(File)

for instruction in ArrayOfInstructions:

    direction = instruction[0]  #this uses string indexing to grab the first character of the string for each element in the array of instructions ie L19 would take the L
    InstructionStringValue = instruction[1:] #this takes the remaing charactoers in the string of instrcuotns ie L19 would take the 19
    InstructionIntegerValue = int(InstructionStringValue)

    if direction == "L":
        currentPosition = (currentPosition - InstructionIntegerValue + 100) % 100
    elif direction == "R":
        currentPosition = (currentPosition + InstructionIntegerValue + 100) % 100
    else:
        print("Something went wrong, neither an L or R was provided")

    #print(currentPosition)

    if currentPosition == 0:
        ZeroPositionCounter += 1

print("The Passcode to the safe is:", ZeroPositionCounter)