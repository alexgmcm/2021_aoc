import sys
import os

def load_input(filepath):
    import re
    f = open(filepath)
    lines = f.readlines()
    pattern = re.compile("([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)")
    processed_input = []
    for i, line in enumerate(lines):
        match = pattern.match(line)
        if (match is None) or (any(map(lambda g: g is None,match.groups()))):
            print(match)
            raise RuntimeError(f"Line {i} of input did not match expected pattern: {line}.")
        else:
            groups = [int(g) for g in match.groups()]
            processed_input.append(((groups[0],groups[1]),(groups[2],groups[3])))
    return processed_input

def filter_hori_vert_lines(proc_input):
    return list(filter(lambda x: (x[0][0] == x[1][0]) or (x[0][1] == x[1][1]),proc_input))

def mark_points(filt_input):
    marked_points = {}
    for line in filt_input:
        if line[0][0] == line[1][0]:
            smaller_x_val = min([line[0][1],line[1][1]])
            greater_x_val = max([line[0][1],line[1][1]])
            for x_val in range(smaller_x_val,greater_x_val + 1):
                point = str((line[0][0],x_val))
                if point in marked_points:
                    marked_points[point] += 1
                else:
                    marked_points[point] = 1
        if line[0][1] == line[1][1]:
            smaller_y_val = min([line[0][0],line[1][0]])
            greater_y_val = max([line[0][0],line[1][0]])
            for y_val in range(smaller_y_val,greater_y_val + 1):
                point = str((y_val,line[0][1]))
                if point in marked_points:
                    marked_points[point] += 1
                else:
                    marked_points[point] = 1
    return marked_points


def main():
    try:
        file_dict = {"test":"test_input",
                    "prod":"input"}
        file_str = file_dict[sys.argv[1]]
    except:
        raise ValueError("Expected second command line argument to specify 'test' or 'prod'")

    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    proc_input = load_input(f"./inputs/{file_str}.txt")
    filt_input = filter_hori_vert_lines(proc_input)
    marked_points = mark_points(filt_input)
    return len(list(filter(lambda x: x>=2, marked_points.values())))

if __name__ == "__main__":       
    print(main())

    
                




        
        

    
