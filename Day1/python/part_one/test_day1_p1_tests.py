from similarity import openone, calculate_total_distance


def test_simplereadtes():
    list_a, list_b = openone("test_input.txt")
    assert list_a
    assert list_b
    assert len(list_a) == 6
    assert len(list_b) == 6
    assert list_a == [3, 4, 2, 1, 3, 3]
    assert list_b == [4, 3, 5, 3, 9, 3]


def test_simpledif():
    list_a, list_b = openone("test_input.txt")
    res = calculate_total_distance(list_a, list_b)

    assert res == 11


def test_myinput():
    list_a, list_b = openone("my_input.txt")
    res = calculate_total_distance(list_a, list_b)

    assert res == 1223326
