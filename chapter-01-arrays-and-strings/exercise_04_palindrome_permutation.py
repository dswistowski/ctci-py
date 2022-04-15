"""
Given a string, write function to check if it is a permatation of palindrome.
"""
import pytest


def palindrome_permutation(word: str) -> bool:
    return _palindrome_permutation(
        list(filter(lambda letter: letter != " ", word.lower())), False
    )


def _palindrome_permutation(elements: list, strict: bool) -> bool:
    if not elements:
        return True
    first = elements[0]
    rest = [e for e in elements if e != first]
    how_many = len(elements) - len(rest)

    if how_many % 2 != 0:
        if strict:
            return False
        return _palindrome_permutation(rest, True)
    return _palindrome_permutation(rest, strict)


def palindrome_permutation_ascii(word: str) -> bool:
    return _palindrome_permutation_ascii(word.lower().encode())


def _palindrome_permutation_ascii(word: bytes) -> bool:
    characters = [0 for _ in range(256)]
    for l in filter(lambda c: c != 32, word):
        characters[l] += 1

    odd = 0
    for c in characters:
        if c % 2 == 1:
            odd += 1

        if odd > 1:
            return False
    return True


def palindrome_permutation_bitvector(word: str) -> bool:
    """Keep index of letter in number as bit, and then make sure there is only one bit toggled"""
    letter_a = b"a"[0]
    letter_z = b"z"[0] - letter_a
    indexes = list(
        filter(
            lambda letter: letter_z > letter > 0,
            (ascii - letter_a for ascii in word.lower().encode()),
        )
    )
    bitvector = 0
    for index in indexes:
        # shift 1 by index to left and do the xor
        bitvector = bitvector ^ (1 << index)

    # if there is one bit on there is no overlap
    # 0001000 - 1 == 000111 & 0001000 == 0
    # 0001010 - 1 == 001001 & 0001010 == 8
    return (bitvector & (bitvector - 1)) == 0


@pytest.fixture(
    params=[
        palindrome_permutation,
        palindrome_permutation_ascii,
        palindrome_permutation_bitvector,
    ]
)
def function_under_test(request):
    return request.param


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("a", True),
        ("Tact Coa", True),
        ("aabbaa", True),
        ("abcd", False),
    ],
)
def test_palindrome_permutation(word, expected, function_under_test):
    assert function_under_test(word) == expected


if __name__ == "__main__":
    print(f'{palindrome_permutation("Tact Coa")=}')
