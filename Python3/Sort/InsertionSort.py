def InsertionSort(InputList):
    start=0
    end=len(InputList)
    for i in range(start, end-1):
        for j in range(start, i+1):
            if InputList[j]>InputList[i+1]:
                InputList.insert(j, InputList[i+1])
                del InputList[i+2]
                break

            
