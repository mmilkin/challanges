from run import almostSorted, can_reverse, can_swap


def helper_test_a(suffix):
    with open('test_input/%s.txt' % suffix, 'r') as f:
        lines = f.readlines()

        arr = lines[1].strip().split(' ')

        out = almostSorted(map(int, arr))

    with open('test_input/expected_%s.txt' % suffix, 'r') as f:
        expected = f.read()
        assert out == expected


def test_one():
    helper_test_a("one")


def test_two():
    helper_test_a("two")


def test_actual_two():
    helper_test_a("actual_two")


def test_reverse():
    arr = [5, 4, 3, 2, 1]
    assert can_reverse(1, arr, sorted(arr)) == (0, 4)


def test_reverse_end():
    arr = [8, 7, 6, 5, 20]
    assert can_reverse(1, arr, sorted(arr)) == (0, 3)


def test_reverse_start_end():
    arr = [3, 8, 7, 6, 5, 20]

    assert can_reverse(2, arr, sorted(arr)) == (1, 4)


def test_can_reverse_2():
    arr = [1, 5, 4, 3, 2,6]
    assert can_reverse(2, arr, sorted(arr)) == (1, 4)


def test_reverse_cant():
    arr = [3, 8, 7, 2, 5, 20]
    assert can_reverse(2, arr, sorted(arr)) is None


def test_reverse_cant_small():
    arr = [3, 1, 2]
    assert can_reverse(1, arr, sorted(arr)) is None


def test_swap_cant():
    arr = [3, 8, 7, 2, 5, 20]
    assert can_swap(2, arr, sorted(arr)) is None


def test_swap_can():
    arr = [23, 21, 30, 33, 50]
    assert can_swap(1, arr, sorted(arr)) == (0, 1)