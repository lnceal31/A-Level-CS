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



