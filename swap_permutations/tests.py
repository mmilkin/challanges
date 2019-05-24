from run import swap_permutation


def helper_test(suffix):
    with open('test_input/%s.txt' % suffix, 'r') as f:
        lines = f.readlines()
        results = []
        number = int(lines[0].strip())
        swaps = int(lines[1].strip())
        results.append(' '.join(map(str, swap_permutation(number, swaps))))
        out = '\n'.join(results)

    with open('test_input/expected_%s.txt' % suffix, 'r') as f:
        lines = f.read()
        assert out == lines.strip()


def test_one():
    helper_test("one")

    # [ 1, 2]
    # [ 2, 1]
    # [1, 2, 3]
    # [1, 3, 2]
    # [2, 1, 3]

    # [1, 2, 3, 4]
    # [2, 1, 3, 4]
    # [1, 3, 2, 4]
    # [1, 2, 4, 3]

    # [1, 2, 3, 4, 5]
    # [2, 1, 3, 4, 5]
    # [1, 3, 2, 4, 5]
    # [1, 2, 4, 3, 5]
    # [1, 2, 3, 5, 4]


def test_xtwo():
    helper_test("two")
