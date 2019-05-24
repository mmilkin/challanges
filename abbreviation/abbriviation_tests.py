from run import abbreviation, Memoize


def helper_test(suffix):
    with open('test_input/%s.txt' % suffix, 'r') as f:
        lines = f.readlines()
        number = lines[0]
        lines = lines[1:]
        value = ""
        for i in range(int(number)):
            value += abbreviation(lines[i*2].strip(), lines[i*2 + 1].strip()) + "\n"
        out = value

    with open('test_input/expected_%s.txt' % suffix, 'r') as f:
        lines = f.readlines()
        assert out == ''.join(lines)


def test_one():
    Memoize.memo = {}
    helper_test("one")


def test_thirteen():
    Memoize.memo = {}
    helper_test("thirteen")

def test_two():
    Memoize.memo = {}
    helper_test("two")

