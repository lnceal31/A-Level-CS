TheData = [20,3,4,8,12,99,4,26,4]

def InsertionSort(TheData):
    for Count in range(0, len(TheData)):
        DataToInsert = TheData[Count]
        Inserted = 0
        NextValue = Count - 1
        while (NextValue >= 0 and Inserted != 1):
            if (DataToInsert < TheData[NextValue]):
                TheData[NextValue+1] = TheData[NextValue]
                NextValue = NextValue-1
                TheData[NextValue+1] = DataToInsert
            else:
                Inserted = 1

def OutputArray(TheData):
    for i in range(0, len(TheData)):
        print(TheData[i])

def main():
    print("Array before sorting:")
    OutputArray(TheData)

    InsertionSort(TheData)
    print("\nArray after sorting:")
    OutputArray(TheData)

def IsFound(number):
    found = False
    for i in range(0, len(TheData)):
        if TheData[i] == number:
            found = True

    if found:
        print("found")
        return True
    else:
        print("not found")
        return False
    
IsFound(8)
IsFound(9)


class HiddenBox():

    # __BoxName String
    # __Creator String
    # __DateHidden String
    # __GameLocation String
    # __LastFinds [10][2] String
    # __Active String
    
    def __init__(self, BoxName, Creator, DateHidden, GameLocation):
        self.__BoxName = BoxName    # String
        self.__Creator = Creator    # String
        self.__DateHidden = DateHidden  # Date
        self.__GameLocation = GameLocation  # String
        self.__LastFinds = [(" ") for i in range(1,10)]
        self.__Active = False     # String

    def GetBoxName(self):
        return self.__BoxName

    def GetGameLocation(self):
        return self.__GameLocation


def main():
    TheBoxes = []
    for i in range(0,len(TheBoxes)):
        TheBoxes = [HiddenBox(" "," "," "," ") for i in range(10000)]
    NewBox[TheBoxes,0]

def NewBox(TheBoxes,NumBoxes):

    Name = input("Enter box name: "))
    Creator = input("Enter box creator: "))
    DateHidden = input("Enter the date the box was hidden: ")
    GameLocation = input("Enter the game location of the box: ")
    
    TheBoxes[NumBoxes] = HiddenBox(Name,Creator,DateHidden,GameLocation)
    NumBoxes += 1
