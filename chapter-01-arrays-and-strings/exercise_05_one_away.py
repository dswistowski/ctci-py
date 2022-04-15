"""
There are three types of edits:
 - insert a character
 - remove a character
 - replace a character
Given two string write function to check if they are one edit away
"""
import pytest


def one_away(s1: str, s2: str) -> bool:
    # the same size - count number of replacements
    if len(s1) == len(s2):
        differences = 0
        for a, b in zip(s1, s2):
            if a != b:
                differences += 1
                if differences > 1:
                    return False
        return True

    # remove to s1 is the same as add to s2
    if len(s1) < len(s2):
        s1, s2 = s2, s1

    len_diff = len(s1) - len(s2)
    if len_diff == 1:
        for i, (a, b) in enumerate(zip(s1, s2)):
            if a != b:
                break
        else:
            return True
        return s1[i + 1:] == s2[i:]
    return False


@pytest.fixture(
    params=[
        one_away,
    ]
)
def function_under_test(request):
    return request.param


@pytest.mark.parametrize(
    "s1,s2,expected",
    [
        ("pale", "ple", True),
        ("pales", "pale", True),
        ("pale", "bale", True),
        ("pale", "bake", False),
    ],
)
def test_one_away(s1, s2, expected, function_under_test):
    assert function_under_test(s1, s2) == expected


if __name__ == "__main__":
    print(f"{one_away('')=}")
