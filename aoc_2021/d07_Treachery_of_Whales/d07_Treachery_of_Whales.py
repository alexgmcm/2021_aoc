import sys
import os

def load_input(filepath):
    f = open(filepath)
    lines = f.readlines()
    horizontal_positions = [int(x) for x in lines[0].split(",")]
    return horizontal_positions

def calc_cost(target_x,horizontal_positions):
    return sum(map(lambda x: abs(x-target_x), horizontal_positions))

def calc_cost_2(target_x,horizontal_positions):
    return sum(map(lambda x: (abs(x-target_x)*(abs(x-target_x)+1))/2, horizontal_positions))

def get_min_cost_x(horizontal_positions):
    candidates = {}
    for target_x in range(min(horizontal_positions), max(horizontal_positions)):
        candidates[target_x] = calc_cost_2(target_x,horizontal_positions)   
    min_x = min(candidates, key=candidates.get)
    return (min_x,candidates[min_x])

def main():
    try:
        file_dict = {"test":"test_input",
                    "prod":"input"}
        file_str = file_dict[sys.argv[1]]
    except:
        raise ValueError("Expected second command line argument to specify 'test' or 'prod'")

    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    horizontal_positions = load_input(f"./inputs/{file_str}.txt")
    return get_min_cost_x(horizontal_positions)

if __name__ == "__main__":       
    print(main())