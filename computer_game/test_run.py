from run import computer_game, item_to_remove, compute_graph, common_factor
from collections import OrderedDict


def helper_test(suffix):
    with open('test_input/%s.txt' % suffix, 'r') as f:
        lines = f.readlines()

        a = map(int, lines[1].strip().split(' '))
        b = map(int, lines[2].strip().split(' '))

        actual = str(computer_game(a, b))

    with open('test_input/expected_%s.txt' % suffix, 'r') as f:
        expected = f.read().strip()
        assert actual == expected


def test_one():
    helper_test("one")


def test_two():
    helper_test("two")


def test_item_to_remove():
    graph = OrderedDict([(2, {4, 6, 10, 14}), (7, {14}), (10, {2, 6, 14}), (6, {10, 2, 14}), (14, {2, 7})])
    assert (7, 14) == item_to_remove(graph)


def test_create_graph_empty():
    actual = compute_graph([], [])
    assert actual == {}


def test_create_graph():
    actual = compute_graph([2, 5, 6, 7], [4, 9, 10, 12])

    expected = {
        2: {12, 10, 4},
        4: {2, 6},
        5: {10},
        6: {9, 10, 4, 12},
        7: set(),
        9: {6},
        10: {2, 5, 6},
        12: {2, 6}
    }
    actual = {k: expected[k] for k in actual if k in expected and expected[k] == actual[k]}
    assert len(actual) == len(expected)


def test_common_factor_False():
    assert common_factor(5, 7) is False


def test_common_factor_True():
    assert common_factor(2, 8) is True



#
# def test_two():
#     helper_test("two")
