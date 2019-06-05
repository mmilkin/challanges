from run import gridland_metro


def helper_test(suffix):
    with open('test_input/%s.txt' % suffix, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

        track = [
            map(int, line.rstrip().split()) for line in lines[1:]
        ]

        n, m, k = map(int, lines[0].split())
        out = str(gridland_metro(n, m, k, track))
    with open('test_input/expected_%s.txt' % suffix, 'r') as f:
        lines = f.read().strip()
        assert out == ''.join(lines)


def test_five():
    helper_test("five")


def test_oxne():
    helper_test("one")


def test_overlap():
    helper_test("two")


def test_three_lap():
    helper_test("three")


def test_seven():
    helper_test("seven")

