from collections import Counter
import csv
def mean(totalWeight,totalEntries):
    mean = totalWeight/totalEntries
    print(mean)
def median(totalEntries,SortedData):
    if totalRows %2 == 0:
        median1 = float(newData[totalEntries//2])
        median2 = float(newData[totalEntries//2-1])
        median = (median1+median2)/2
    else:
        median = newData[totalEntries//2]
    print(median)
def mode(SortedData):
    data = Counter(newData)
    modeDataRange = {
        "75-85":0,
        "85-95":0,
        "95-105":0
        "105-115":0
        "115-125":0
        "125-135":0
        "135-145":0
        "145-155":0
        "155-165":0
        "165-175":0
    }  
    for height,occurance in data.items():
        if 75<float(height)<85:
        modeDataRange["75-85"]+=occurance
        elif 85<float(height)<95:
        modeDataRange["85-95"]+=occurance
        elif 95<float(height)<105:
        modeDataRange["95-105"]+=occurance
        elif 105<float(height)<115
        modeDataRange["105-115"]+=occurance
        elif 105<float(height)<115
        modeDataRange["105-115"]+=occurance

        
modeRange,modeOccurance = 0,0
for range,occurance in modeDataRange.items():
    if occurance>modeOccurance:
        modeRange,modeOccurance = [int(range.split("-")[0]),int(range.split("-")[1])],occurance
mode = float((modeRange[0] + modeRange[1]) / 2)
print(mode)
    


