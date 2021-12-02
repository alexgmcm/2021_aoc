def main():
    with open('input.txt') as f:
        x = 0
        y = 0
        
        lines = f.readlines()
        lines = list(map(lambda x: x.split(),lines))
        for i,line in enumerate(lines):
            #print(f"{i}: {line}")
            if len(line)!=2:
                raise ValueError(f"Expected line {i} to have two elements: {line}")
            cmd = line[0]
            val = line[1]
            if cmd == "forward":
                x += int(val)
            elif cmd == "down":
                y += int(val)
            elif cmd == "up":
                y -= int(val)
            else:
                raise ValueError(f"Unrecognised command: {cmd}")
         
        print(x*y)
main()