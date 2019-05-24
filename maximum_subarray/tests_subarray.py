from run import maxSubarray


def helper_test(suffix):
    out = ''
    with open('test_input/%s.txt' % suffix, 'r') as f:
        lines = f.readlines()
        for i in range(len(lines[1:]) / 2):
            array = map(int, lines[2 + i * 2].strip().split(' '))
            out += str(maxSubarray(array)) + '\n'

    with open('test_input/expected_%s.txt' % suffix, 'r') as f:
        lines = f.readlines()
        assert out.strip() == ''.join(lines).strip()


def test_one():
    helper_test("one")


def test_me():
    assert "twenty five minutes to seven" == timeInWords(6, 35)


def test_two():
    helper_test("two")


CONVERT_TENS = {
    2: "twenty"
}

CONVERT_NUMBER = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    0: "o' clock",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "quarter",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "half"
}


def to_string(n):
    if n in CONVERT_NUMBER:
        return CONVERT_NUMBER[n]
    tens = n / 10
    ones = n - tens * 10
    return "AAAAA"
    #return "%s %s" % (CONVERT_TENS.get(tens), CONVERT_NUMBER[ones])

# Complete the timeInWords function below.
def timeInWords(h, m):

    with_to = "%s minute%s to %s"
    with_past = "%s minute%s past %s"
    to = "%s to %s"
    past = "%s past %s"

    if m == 30:
        return "half past " + to_string(h)
    elif m == 0:
        return to_string(h) + " " + to_string(m)
    elif m < 30:
        if m != 15:
            return with_past % (to_string(m), "s" if m != 1 else "", to_string(h))
        else:
            return past % (to_string(m), to_string(h))
    else:
        h = h + 1 if h + 1 <= 12 else 1
        minutes = 60 - m
        if minutes != 15:
            return with_to % (to_string(minutes), "s" if m != 1 else "", to_string(h))
        else:
            return to % (to_string(minutes), to_string(h))
