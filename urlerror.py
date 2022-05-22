import re 
import collections
import sys 

def _url(name_file):
    urls = []
    with open(name_file) as file:
        for line in file.readlines():
            url = re.findall(r"(?:/[^/]+)+?/\w+\.\w+", line)
            if len(url) == 2:
                urls.append(url[0] + url[1])
        
        occ = collections.Counter(urls)

        defaults = 0
        for key in occ:
            print("{} {}".format(key, occ[key]))
            defaults = defaults + occ[key]
        
        print("{} url en défaut".format(defaults))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        _url(sys.argv[1])
    else:
        print("File required!")