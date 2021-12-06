from aoc_2021.d05_HydrothermalVenture.d05_HydrothermalVenture_2 import load_input, filter_hori_vert_lines, mark_points

def test_load_input():
    filepath = "aoc_2021/d05_HydrothermalVenture/inputs/test_input.txt"
    processed_input = load_input(filepath)
    assert processed_input[0] == ((0,9),(5,9))
    assert len(processed_input) == 10

def test_filter_hoz_ver():
    filepath = "aoc_2021/d05_HydrothermalVenture/inputs/test_input.txt"
    processed_input = load_input(filepath)
    filtered_lines = filter_hori_vert_lines(processed_input)
    assert filtered_lines == [((0,9),(5,9)),
                            ((9,4),(3,4)),
                            ((2,2),(2,1)),
                            ((7,0),(7,4)),
                            ((0,9),(2,9)),
                            ((3,4),(1,4))]

def test_mark_points_filtered():
    filtered_lines = [((0,9),(5,9)),
                            ((9,4),(3,4)),
                            ((2,2),(2,1)),
                            ((7,0),(7,4)),
                            ((0,9),(2,9)),
                            ((3,4),(1,4))]
    marked_points = mark_points(filtered_lines)
    #print(marked_points)
    assert len(marked_points.items()) == 2+4+9+6
    assert len(list(filter(lambda x: x>=2,marked_points.values()))) == 5

def test_mark_points_unfiltered_full():
    filepath = "aoc_2021/d05_HydrothermalVenture/inputs/test_input.txt"
    processed_input = load_input(filepath)
    marked_points = mark_points(processed_input)
    print(marked_points)
    assert len(marked_points.items()) == 4+4+5+3+9+2+2+2+2+6
    assert len(list(filter(lambda x: x>=2,marked_points.values()))) == 12
    assert True

def test_mark_points_unfiltered_partial():
    processed_input = [((1,1),(3,3))]
    processed_input2 = [((9,7),(7,9))]
    marked_points = mark_points(processed_input)
    assert list(marked_points.keys()) == ["[1, 1]", "[2, 2]", "[3, 3]"]

    marked_points2 = mark_points(processed_input2)
    assert list(marked_points2.keys()) == ["[9, 7]", "[8, 8]", "[7, 9]"]
    #assert len(list(filter(lambda x: x>=2,marked_points.values()))) == 0


    

    

