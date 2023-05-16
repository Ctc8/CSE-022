#1
def maxInRange(someList, start, end):
    return max (someList[start:end+1])

#2
def minInRange(someList, start, end):
    return min (someList[start:end+1])

#3
def elementCounter(someList, element):
    count = 0
    for num in someList:
        if num == element:
            count = count + 1
    return count

#4
def elementPos(someList, element):
    pos = []
    for num in range(len(someList)):
       if someList[num] == element:
           pos = pos + [num]
    return pos

#5
def ranges(sortedList):
    ranges = []
    if len(sortedList) == 0:                    # condition if the entered list is blank
        return ranges

    start = sortedList[0]
    end = sortedList[0]
    for i in range(len(sortedList)-1):
        if sortedList[i] + 1 == sortedList[i+1]:
            end = sortedList[i+1]
        else:
            ranges = ranges + [(start, end)]
            start = sortedList[i+1]
            end = sortedList[i+1]
    return ranges + [(start, end)]

#6
def occupySlot(sequence):
    for i in range(len(sequence)):
        if i == 0 and sequence[i+1] == 0:
            sequence[i] = 1
        elif i == len(sequence)-1 and sequence[i-1] == 0:
            sequence[i] = 1
        elif i > 0 and i < len(sequence)-1 and sequence[i-1] == 0 and sequence[i+1] == 0:
            sequence[i] = 1
    return sequence

#7
def setMismatch(someList):
    for i in range(len(someList)):
        if someList[i] != i+1:
            return (someList[i], i+1)

if __name__ == "__main__":
    print (maxInRange([1,2,3,4,5,6,7,8], 1, 3))         # 4
    print (maxInRange([1,20,3,4,5,6,7,8], 1, 3))        # 20
    print (minInRange([1,2,3,4,5,6,7,8], 1, 3))         # 2
    print (minInRange([1,0,3,4,5,6,7,8], 1, 3))         # 0
    print (minInRange([1,0,3,-1,5,6,7,8], 1, 3))        # -1
    print (elementCounter([1,3,1,4,1,5,1,6,1,7], 1))    # 5
    print (elementPos([1,3,1,4,1,5,1,6,1,7], 1))        # [0, 2, 4, 6, 8]
    print (ranges([0,1,2,4,5,7]))                       # [(0, 2), (4, 5), (7, 7)]
    print (ranges([1,2,3,4,5,6,7,8]))                   # [(1, 8)]
    print (ranges([0,2,3,4,6,8,9]))                     # [(0, 0), (2, 4), (6, 6), (8, 9)]
    print (ranges([]))                                  # []
    print (ranges([4]))                                 # [(4, 4)]
    print (occupySlot([0,1,1,0,0]))                     # [0, 1, 1, 0, 1]
    print (occupySlot([0,0,0,0,0]))                     # [1, 0, 1, 0, 1]
    print (occupySlot([0,1,0,0,0]))      
    print (setMismatch([1,1]))                          # (1, 2)
    print (setMismatch([1,2,2,4]))                      # (2, 3)
    print (setMismatch([1,2,3,4,5,9,7,8,9,10]))         # (9, 6)





