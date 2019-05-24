from .run import bfs


def helper_test(suffix):
    out = ''

    with open('test_input/%s.txt' % suffix, 'r') as f:
        lines = f.readlines()
        t = int(lines[0])
        cursor = 1
        for t_itr in range(t):
            nm = lines[cursor].split()
            cursor += 1
            n = int(nm[0])

            m = int(nm[1])

            edges = []

            for i in range(m):
                edges.append(list(map(int, lines[cursor].rstrip().split())))
                cursor += 1

            start = int(lines[cursor])
            cursor += 1

            result = bfs(n, edges, start)
            out = '%s%s\n' % (out, ' '.join(map(str, result)))

    with open('test_input/xxx%s.txt' % suffix, 'w') as z, \
            open('test_input/expected_%s.txt' % suffix, 'r') as f:
        expected = f.read()
        z.write(out)
        assert out.strip() == expected


def test_one():
    helper_test("one")
