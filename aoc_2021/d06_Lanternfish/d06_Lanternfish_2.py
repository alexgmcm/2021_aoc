import sys
import os
import copy
import collections

def load_input(filepath):
    import re
    f = open(filepath)
    lines = f.readlines()
    lanternfish = [int(x) for x in lines[0].split(",")]
    lanternfish_dict = collections.Counter(lanternfish)
    return lanternfish_dict

def iterate(lanternfish):
    lanternfish_copy = copy.deepcopy(lanternfish)
    max_key = max(lanternfish.keys())
    for i in range(max_key,0,-1):
        try:
            lanternfish_copy[i-1] = lanternfish[i]
        except KeyError:
            lanternfish_copy[i-1] = 0
    lanternfish_copy[max_key] = 0
    lanternfish_copy[8] = lanternfish[0]
    lanternfish_copy[6] += lanternfish[0]
    return lanternfish_copy

def main():
    try:
        file_dict = {"test":"test_input",
                    "prod":"input"}
        file_str = file_dict[sys.argv[1]]
    except:
        raise ValueError("Expected second command line argument to specify 'test' or 'prod'")

    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    lanternfish = load_input(f"./inputs/{file_str}.txt")
    n_lanternfish = []
    n_lanternfish.append(sum(lanternfish.values()))
    for day in range(256):
        lanternfish = iterate(lanternfish)
        n_lanternfish.append(sum(lanternfish.values()))
    print(lanternfish)
    return n_lanternfish

if __name__ == "__main__":       
    n_lanternfish = main()
    #print(n_lanternfish)
    print(n_lanternfish[256])