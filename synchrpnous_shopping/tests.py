from run import shop


def helper_test(suffix):
    with open('test_input/%s.txt' % suffix, 'r') as f:
        lines = f.readlines()

        r, c, n = map(int, lines[0].strip().split(' '))

        grid = [
            list(line.strip().split(' ')) for line in lines[1: n + 1]
        ]

        roads = [
            list(line.strip().split(' ')) for line in lines[n + 1:]
        ]

        out = str(shop(int(r), int(c), grid, roads))

    with open('test_input/expected_%s.txt' % suffix, 'r') as f:
        line = f.read().strip()
        assert out == line


def test_one():
    helper_test("one")


