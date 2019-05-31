from run import encryption


def helper_test(suffix):
    with open('test_input/%s.txt' % suffix, 'r') as f:
        phrase = f.read().strip()
        out = encryption(phrase)
    with open('test_input/expected_%s.txt' % suffix, 'r') as f:
        lines = f.read().strip()
        assert out == ''.join(lines)


def test_zero():
    helper_test("zero")


def test_one():
    helper_test("one")


def test_two():
    helper_test("two")

