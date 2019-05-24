from run import bomber_man


def helper_test(suffix):
    with open('test_input/%s.txt' % suffix, 'r') as f:
        lines = f.readlines()

        r, c, n = lines[0].strip().split(' ')

        grid = [
            list(line.strip()) for line in lines[1:]
        ]

        new_grid = bomber_man(int(r), int(c), int(n), grid)

        out_gird = [''.join(
            [item if item == '.' else 'O' for item in row]
        ) for row in new_grid]

        out = '\n'.join(out_gird)

    with open('test_input/expected_%s.txt' % suffix, 'r') as f:
        lines = f.readlines()
        assert out == ''.join(lines)


def test_one():
    helper_test("one")


def test_two():
    helper_test("two")


def test_nineteen():
    helper_test("nineteen")
