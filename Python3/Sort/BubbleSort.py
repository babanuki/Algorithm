def BubbleSort(InputList):
    start=0
    end=len(InputList)
    for i in range(start, end):
        for j in range(start, end-1-i):
            if InputList[j]>InputList[j+1]:
                InputList[j], InputList[j+1]=InputList[j+1], InputList[j]

