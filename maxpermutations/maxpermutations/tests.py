from run import absolutePermutation


def helper_test(suffix):
    with open('test_input/%s.txt' % suffix, 'r') as f:
        lines = f.readlines()

        n = lines[0].strip()
        out = ''
        for i in range(1, int(n) + 1):
            n, k = lines[i].strip().split(' ')
            result = absolutePermutation(int(n), int(k))
            out += '\n'.join(' '.join(map(str, result)))

    with open('test_input/expected_%s.txt' % suffix, 'r') as f:
        lines = f.readlines()
        assert out == ''.join(lines)


def test_one():
    helper_test("one")


def test_two():
    helper_test("two")
