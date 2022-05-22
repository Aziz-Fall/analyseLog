import re 
import collections
import sys
from datetime import datetime

def getdate(line):
    items = line.split(" ")
    if len(items[2]) == 0:
        items[5] = items[5].replace("]","")
        return items[1] + "," + items[3] + "," + items[5]

    items[4] = items[4].replace("]","")
    return items[1] + "," + items[2] + "," + items[4]

def geturl(line):
    line = line.split(" ")
    return line[- 1].rstrip("\n")


def _url(name_file):
    urls = {}
    with open(name_file) as file:
        line = file.readline()
        for line in file.readlines():
            url = geturl(line)
            date = getdate(line)
            date = datetime.strptime(date, "%b,%d,%Y").strftime("%d/%m/%Y")

            if url not in urls:
                urls[url] = []
            
            urls[url].append(date)
             
        occ = collections.Counter(urls)
        for keys in urls:
            dates = urls[keys]
            occ = collections.Counter(dates)
            total = 0
            for item in occ:
                total = total + occ[item]
            dates = list(dict.fromkeys(dates))

            if len(dates) == 1:
                print("{} {} {}".format(keys, total, dates[-1]))
            else:
                print("{} {} {} {}".format(keys, total, dates[0], dates[-1]))
        

if __name__ == "__main__":
    if len(sys.argv) == 2:
        _url(sys.argv[1])
    else:
        print("File required!")