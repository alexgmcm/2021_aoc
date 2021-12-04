# Gamma rate is constructed from most common bit in each position
# Epsilon rate is constructed from least common bit in each position
# Return gamma_rate * epsilon_rate (in decimal)

#part 2
# filter from left to right numbers that match bits of gamma for oxygen gen rating
# filter from left to right numbers that match bits of epsilon for CO2 scrubber rating
# no its harder as you are excluding numbers as you iterate
# return product of the found values

import sys
import os

def determine_most_common_bit(pos,lines):
    n_bits = len(lines[0].strip())
    if pos >= n_bits:
        raise ValueError(f"bit position {pos} expected to be smaller than n_bits {n_bits}")
    n_lines= len(lines)
    bit_count = 0
    threshold = n_lines/2
    for line in lines:
        bit_count += int(line[pos])
    if bit_count>=threshold:
        return 1
    elif bit_count<threshold:
        return 0
    else:
        raise ValueError(f"bit_count {bit_count} could not be compared to threshold {threshold}")


def get_rating(type, lines):
    n_bits = len(lines[0].strip())
    remaining_lines = lines
    oxy_gen_cond = lambda x: int(x[pos]) == mcb
    co2_scr_cond = lambda x: int(x[pos]) != mcb
    cond_dict = {"oxy":oxy_gen_cond,
                "co2":co2_scr_cond}
    #scan through bits from left to right
    for pos in range(n_bits):
        mcb = determine_most_common_bit(pos,remaining_lines)
        remaining_lines = list(filter(cond_dict[type],remaining_lines))
        if len(remaining_lines) == 1:
            return remaining_lines[0]
    raise RuntimeError(f"Never reached single candidate in remaining_lines: {remaining_lines}")

def convert_rating_to_dec(rating):
    return int(rating.strip(),base=2)



def main():
    try:
        file_dict = {"test":"test_input",
                    "prod":"input"}
        file_str = file_dict[sys.argv[1]]
    except:
        raise ValueError("Expected second command line argument to specify 'test' or 'prod'")
    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    os.chdir(path)

    with open(f'../inputs/{file_str}.txt') as f:
        # Get number of bits
        lines = f.readlines()
        n_lines = len(lines)

        oxy_gen_rating = get_rating("oxy",lines)
        co2_scr_rating = get_rating("co2",lines)
        
        oxy_gen_rating_dec = convert_rating_to_dec(oxy_gen_rating)
        co2_scr_rating_dec = convert_rating_to_dec(co2_scr_rating)
        print(oxy_gen_rating_dec * co2_scr_rating_dec )

        


if __name__ == "__main__":       
    main()
