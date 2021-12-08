from aoc_2021.d08_SevenSegmentSearch.SevenSegmentSearch import load_input, count_1478

def test_load_input():
    expected_input = (["be","cfbegad","cbdgef","fgaecd", "cgeb", "fdcge", "agebfd", "fecdb", "fabcd", "edb"],["fdgacbe", "cefdb", "cefbgd", "gcbe"])
    total_input = load_input("aoc_2021/d08_SevenSegmentSearch/inputs/test_input.txt")
    assert total_input[0] == expected_input


def test_count_1478():
    input = load_input("aoc_2021/d08_SevenSegmentSearch/inputs/test_input.txt")
    assert count_1478(input) == 26