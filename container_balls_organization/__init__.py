from collections import defaultdict


def run(query):
    balls_per_row = []
    balls_of_type = defaultdict(int)

    for item in query:
        balls_per_row.append(sum(item))
        for i in range(len(item)):
            balls_of_type[int(i)] += int(item[i])

    balls_of_type = sorted(balls_of_type.values())
    balls_per_row = sorted(balls_per_row)

    if balls_of_type == balls_per_row:
        print 'Possible'
        return
    print 'Impossible'


def parse_query():
    query = []
    for _ in range(int(raw_input())):
        query.append(
            [int(i) for i in raw_input().split(" ")]
        )
    return query


if __name__ == '__main__':
    n = int(raw_input())
    for item in range(n):
        run(parse_query())
