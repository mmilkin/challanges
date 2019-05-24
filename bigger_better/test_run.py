import run


def test_input_one():
    # assert "ba" == run.me("ab")
    # assert "no answer" == run.me("bb")
    assert "hegf" == run.me("hefg")
    # abcdefgh
    assert "dhkc" == run.me("dhck")
    assert "hcdk" == run.me("dkhc")
