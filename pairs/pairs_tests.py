from run import pairs


def helper_test(suffix):
    with open('test_input/%s.txt' % suffix, 'r') as f:
        lines = f.readlines()
        n, k = lines[0].strip().split(' ')

        items = [
            int(i) for i in list(lines[1].strip().split(' '))
        ]

        k = int(k)
        out = pairs(k, items)

    with open('test_input/%s_expected.txt' % suffix, 'r') as f:
        lines = f.readlines()
        assert str(out) == ''.join(lines)


def test_one():
    helper_test("one")


