from run import candies


def helper_test(suffix):
    with open('test_input/%s.txt' % suffix, 'r') as f:
        lines = f.readlines()

        children = [
            int(line.strip()) for line in lines[1:]
        ]

        value = candies(len(children) , children)
        out = str(value)

    with open('test_input/expected_%s.txt' % suffix, 'r') as f:
        lines = f.readlines()
        assert out == ''.join(lines)


def test_one():
    helper_test("one")


def test_two():
    helper_test("two")

