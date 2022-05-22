import sys
import re 
import matplotlib.pyplot as plt 

regex_nav = r"(MSIE|(?!Gecko.+)Firefox|(?!AppleWebKit.+Chrome.+)Safari|(?!AppleWebKit.+)Chrome|AppleWebKit(?!.+Chrome|.+Safari)|Gecko(?!.+Firefox))(?: |\/)([\d\.apre]+)"
regex_sys = r"(Mac OS|Linux|Windows)"

def get_nav_connect(name_file):
    occ_connect_nav = {}
    occ_connect_sys = {}
    with open(name_file) as file:
            line = file.readline()
            for line in file.readlines():
                nav = re.findall(regex_nav, line)
                system = re.findall(regex_sys, line)
                if len(nav): 
                    if nav[0][0] not in occ_connect_nav:
                        occ_connect_nav[nav[0][0]] = 1
                    else:
                        occ_connect_nav[nav[0][0]] = occ_connect_nav[nav[0][0]] + 1
                if len(system): 
                    if system[0] not in occ_connect_sys:
                        occ_connect_sys[system[0]] = 1
                    else:
                        occ_connect_sys[system[0]] = occ_connect_sys[system[0]] + 1
    return occ_connect_nav, occ_connect_sys

def display_pie(nav_connect, sys_connect):
    nav = []
    nb_nav_connects = []
    system = []
    nb_sys_connects = []

    for n, c in nav_connect.items():
        nav.append(n)
        nb_nav_connects.append(c)
    
    for s, c in sys_connect.items():
        system.append(s)
        nb_sys_connects.append(c)

    plt.figure(0)
    plt.pie(nb_nav_connects, labels=nav)
    plt.figure(1)
    plt.pie(nb_sys_connects, labels=system)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        nav_connect, sys_connect = get_nav_connect(sys.argv[1]) 
        display_pie(nav_connect, sys_connect)
    else:
        print("File required!")
