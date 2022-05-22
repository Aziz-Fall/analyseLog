import sys
from datetime import datetime
import collections

def getdate(line):
    items = line.split(" ")
    if len(items[2]) == 0:
        items[5] = items[5].replace("]","")
        return items[1] + "," + items[3] + "," + items[5]

    items[4] = items[4].replace("]","")
    return items[1] + "," + items[2] + "," + items[4]

def read_date(name_file):
    dates = []
    with open(name_file) as file:
        for line in file.readlines():
            date = getdate(line)
            
            date = datetime.strptime(date, '%b,%d,%Y').strftime("%d/%m/%Y")
            dates.append(date)
            
    return dates 


if __name__ == "__main__":
    if len(sys.argv) == 2:
        dates = read_date(sys.argv[1]) 
        occu = collections.Counter(dates)
        sums = 0
        for key in occu:
            print("{} {}".format(key, occu[key]))
            sums = sums + occu[key]
        print("Moyenne: {}".format(round(sums/len(occu), 2)))
    else:
        print("File required!")
