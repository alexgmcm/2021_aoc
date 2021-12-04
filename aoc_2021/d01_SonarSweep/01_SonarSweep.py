def main():
    with open('input.txt') as f:
        lines = f.readlines()
        lines = list(map(int,lines))
        #print(len(lines))
        print(sum([1 if y>x else 0 for y,x in zip(lines[1:],lines[:-1])]))
        print( len([1 if y>x else 0 for y,x in zip(lines[1:],lines[:-1])]) )
main()