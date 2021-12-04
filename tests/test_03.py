import pytest
from aoc_2021.d03_BinaryDiagnostic.part2.d03_BinaryDiagnostic_2 import determine_most_common_bit, get_rating, convert_rating_to_dec

@pytest.fixture
def test_input():
    f=open('aoc_2021/d03_BinaryDiagnostic/inputs/test_input.txt') 
    lines = f.readlines()
    f.close()
    return lines

def test_determine_mcb(test_input):
    assert determine_most_common_bit(0,test_input) == 1
    assert determine_most_common_bit(1,test_input) == 0

def test_get_rating(test_input):
    assert get_rating("oxy",test_input).strip() == "10111"
    assert get_rating("co2",test_input).strip() == "01010"

def test_convert_rating_to_dec():
    assert convert_rating_to_dec("10111\n") == 23
    assert convert_rating_to_dec("01010\n") == 10