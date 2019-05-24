

def solve(graph):
    connections = {}
    rows = len(graph)
    columns = len(graph[0])
    row_os = [set() for _ in range(columns)]
    column_os = [set() for _ in range(columns)]
    for row in range(rows):
        for col in range(columns):
            if graph[row][col] == 'O':
                row_os[row].add((row, col))
                column_os[col].add((row, col))

    pass


def test_solve():
    solve(
        [
            ['X', 'X', 'O', 'X', 'X', 'O'],
            ['O', 'X', 'X', 'X', 'X', 'X'],
            ['O', 'X', 'X', 'X', 'X', 'O'],
            ['X', 'X', 'O', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'X', 'X', 'O']
        ])
