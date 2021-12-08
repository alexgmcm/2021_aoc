import os
import sys

def load_input(filepath):
    f = open(filepath)
    lines = f.readlines()
    lines = [line.split("|") for line in lines]
    lines = [(line[0].split(),line[1].split()) for line in lines]
    return lines

def count_1478(input):
    # only 1 has 2 segs, only 4 has 4 segs, only 7 has 3 segs, only 8 has 8 segs
    count=0
    for entry in input:
        #print(entry)
        count += len(list(filter(lambda segs: len(segs) in [2,4,3,7], entry[1])))
    return count

candidates = {"top":set(),"top_left":set(),"top_right":set(),"mid":set(),"bottom_left":set(),"bottom_right":set(),"bottom":set()}
# start with seg_code that has len=2 and add it's letters as candidates for top_right,bottom_right
# then get seg_code with len=3 and add it's letters and candidates for top_right,bottom_right, top

# letter in seg code for len3 but not len2, must be top segment
# 


def main():
    try:
        file_dict = {"test":"test_input",
                    "prod":"input"}
        file_str = file_dict[sys.argv[1]]
    except:
        raise ValueError("Expected second command line argument to specify 'test' or 'prod'")

    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    input = load_input(f"./inputs/{file_str}.txt")
    return count_1478(input)

if __name__ == "__main__":       
    print(main())
