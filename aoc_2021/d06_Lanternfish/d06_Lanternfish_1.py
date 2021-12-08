import sys
import os
import copy

def load_input(filepath):
    import re
    f = open(filepath)
    lines = f.readlines()
    lanternfish = [int(x) for x in lines[0].split(",")]
    return lanternfish


def iterate(lanternfish):
    lanternfish_copy = copy.deepcopy(lanternfish)
    for ind, val in enumerate(lanternfish):
        if val == 0:
            lanternfish_copy[ind] = 6
            lanternfish_copy.append(8)
        else: 
            lanternfish_copy[ind] = val-1
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
    n_lanternfish.append(len(lanternfish))
    for day in range(256):
        lanternfish = iterate(lanternfish)
        n_lanternfish.append(len(lanternfish))
    return n_lanternfish

if __name__ == "__main__":       
    n_lanternfish = main()
    print(n_lanternfish[256])

