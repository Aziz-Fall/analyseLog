import sys
import re 
import matplotlib.pyplot as plt 

regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

def getip(name_file):
    occ_ips = {}
    with open(name_file) as file:
            line = file.readline()
            for line in file.readlines():
                ip = re.findall(regex, line)
                if len(ip): 
                    if ip[0] not in occ_ips:
                        occ_ips[ip[0]] = 1
                    else:
                        occ_ips[ip[0]] = occ_ips[ip[0]] + 1
    return occ_ips

def classip(occ_ips):
    occ_class = {
        "classe A": 0, 
        "classe B": 0,
        "classe C": 0,
        "autres": 0
    }
    for ip in occ_ips:
        rank = int(ip.split(".")[0])
        if rank in range(1, 127):
           occ_class["classe A"] = occ_class["classe A"] + occ_ips[ip]
        elif rank in range(128, 191):
            occ_class["classe B"] = occ_class["classe B"] + occ_ips[ip]
        elif rank in range(192, 223):
            occ_class["classe C"] = occ_class["classe C"] + occ_ips[ip]
        else:
            occ_class["autres"] = occ_class["autres"] + occ_ips[ip]
    return occ_class

def display_class(occ_class):
    for keys in occ_class:
        print("{} {}".format(keys, occ_class[keys]))

def display_pie(occ_class):
    ip_class = []
    nb_connects = []

    for l, s in occ_class.items():
        ip_class.append(l)
        nb_connects.append(s)
    
    plt.pie(nb_connects, labels=ip_class)
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        occ_class = classip(getip(sys.argv[1]))
        display_class(occ_class)
        display_pie(occ_class)
    else:
        print("File required!")

