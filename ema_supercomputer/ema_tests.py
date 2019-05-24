from run import two_pluses


def helper_test(suffix):
    with open('test_input/%s.txt' % suffix, 'r') as f:
        lines = f.readlines()

        n, m = lines[0].strip().split(' ')

        grid = [
            list(line.strip()) for line in lines[1:]
        ]

        out = two_pluses(grid)

    with open('test_input/%s_expected.txt' % suffix, 'r') as f:
        lines = f.readlines()
        assert out == ''.join(lines)


def test_one():
    helper_test("one")


def test_two():
    helper_test("two")

