from run import mandragora


def helper_test(suffix):
    with open('test_input/%s.txt' % suffix, 'r') as f:
        lines = f.readlines()

        t = int(lines[0].strip())
        outs = []
        for i in range(1, t + 1):
            h = map(int, lines[i * 2].strip().split(' '))
            outs = mandragora(h)
            outs.append(outs)

        out = '\n'.join(outs)

    with open('test_input/expected_%s.txt' % suffix, 'r') as f:
        lines = f.read().strip()
        assert out == ''.join(lines)


def test_one():
    helper_test("one")


def test_two():
    helper_test("two")
