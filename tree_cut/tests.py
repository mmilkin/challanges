from .run import cut_the_tree


def helper_test(suffix):
    out = ''

    with open('test_input/%s.txt' % suffix, 'r') as f:
        lines = f.readlines()
        nodes = int(lines[0])
        values = map(int, lines[1].strip().split(' '))
        edges = [
            map(int, x.strip().split(" ")) for x in lines[2:]
        ]
        out += str(cut_the_tree(values, edges))
    with open('test_input/expected_%s.txt' % suffix, 'r') as f:
        expected = f.read()
        assert out.strip() == expected


def test_two():
    helper_test("two")


def test_one():
    helper_test("one")
