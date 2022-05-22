import sys
import re 
import matplotlib.pyplot as plt 

regex_date = r"\d{1,2}\/[A-Za-z]{1,3}\/[0-9]{4}"

def get_nb_connect(name_file):
    occ_connect = {}
    with open(name_file) as file:
            line = file.readline()
            for line in file.readlines():
                date = re.findall(regex_date, line)
                if len(date): 
                    new_date = date[0].split("/")
                    new_date = new_date[1] + "/" + new_date[-1]
                    if new_date not in occ_connect:
                        occ_connect[new_date] = 1
                    else:
                        occ_connect[new_date] = occ_connect[new_date] + 1

    return occ_connect

def display_plot(nb_connects):
    dates = []
    nb_connect = []

    for l, s in nb_connects.items():
        dates.append(l)
        nb_connect.append(s)

    plt.xlabel("Dates")
    plt.xticks(rotation=85)
    plt.ylabel("Nombre de connexions")
    plt.plot(dates, nb_connect, label="line 1")
    plt.show()

def display_connects(occ_connects):
    for date, nb_occ in occ_connects.items():
        print("{} {}".format(date, nb_occ))
    
if __name__ == "__main__":
    if len(sys.argv) == 2:
        nb_connects = get_nb_connect(sys.argv[1]) 
        display_connects(nb_connects)
        display_plot(nb_connects)
    else:
        print("File required!")