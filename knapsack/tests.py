from run import unbounded_knapsack


def helper_test(suffix):
    with open('test_input/%s.txt' % suffix, 'r') as f:
        lines = f.readlines()

        n = int(lines[0].strip())
        results = []
        for i in range(n):
            target = map(int, lines[2*i+1].strip().split(' '))[1]
            numbers = sorted(map(int, lines[2*i+2].strip().split(' ')))
            results.append(str(unbounded_knapsack(target, numbers)))

        out = '\n'.join(results)

    with open('test_input/expected_%s.txt' % suffix, 'r') as f:
        lines = f.read()
        assert out == lines.strip()


def test_xone():
    helper_test("one")


def test_xtwo():
    helper_test("two")
