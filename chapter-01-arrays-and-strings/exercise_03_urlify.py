"""
Write a method to replace all spaces in a string with '%20'

Note:
    this is trivial in python, so assuming it will use character array to emulate other languages problems
"""


def urlify(input: bytes, size: int, fillter=b"%20") -> bytes:
    # last letter position
    poz = -1
    letters = list(input)
    for letter in letters[:size]:
        if letter == 32:
            poz += len(fillter)
        else:
            poz += 1

    for letter in reversed(letters[:size]):
        if letter != 32:
            letters[poz] = letter
            poz -= 1
        else:
            for i, letter in enumerate(reversed(fillter)):
                letters[poz - i] = letter
            poz -= len(fillter)

    return bytes(letters)


def test_urlify():
    assert urlify(b"Mr John Smith    ", 13) == b"Mr%20John%20Smith"


if __name__ == "__main__":
    print(urlify(b"Mr John Smith    ", 13))
