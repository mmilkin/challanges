from run import get_cost


def helper_test(suffix):
    with open('test_input/%s.txt' % suffix, 'r') as f:
        lines = f.readlines()
        g_nodes, g_edges = map(int, lines[0].strip().split(' '))

        nodes = [
            map(int, line.strip().split(' ')) for line in lines[1:]
        ]

        value = get_cost(nodes, 1, g_nodes)
        out = str(value)

    with open('test_input/expected_%s.txt' % suffix, 'r') as f:
        lines = f.readlines()
        assert out == ''.join(lines)


def test_one():
    helper_test("one")


def test_two():
    helper_test("two")

