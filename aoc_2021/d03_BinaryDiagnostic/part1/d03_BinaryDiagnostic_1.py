# Gamma rate is constructed from most common bit in each position
# Epsilon rate is constructed from least common bit in each position
# Return gamma_rate * epsilon_rate (in decimal)

def main():
    with open('../inputs/test_input.txt') as f:
        # Get number of bits
        lines = f.readlines()
        n_lines = len(lines)
        n_bits = len(lines[0].strip())
        #print(n_bits)

        bit_counts = []
        # init bit counts array
        for i in range(0,n_bits):
            bit_counts.append(0)

        threshold = n_lines / 2
       
        for line_no,line in enumerate(lines):
            #print(line)
            for i in range(0,n_bits):
                #print(i)
                bit_counts[i] += int(line[i])

        #pt1 code
        gamma = list(map(lambda x: 1 if x>threshold else 0 , bit_counts))
        epsilon = list(map(lambda x: 0 if x==1 else 1, gamma))

        gamma_dec = int("".join([str(i) for i in gamma]),base=2)
        epsilon_dec = int("".join([str(i) for i in epsilon]),base=2)

        print(gamma_dec * epsilon_dec) # part 1

        
main()
