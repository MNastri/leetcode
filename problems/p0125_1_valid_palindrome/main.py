"""Checks if a phrase is a palindrome."""
from string import (
    ascii_lowercase,
    digits,
)

ALLOWED_CHARS = ascii_lowercase + digits


def is_palindrome(text: str, allowed_chars: str) -> bool:
    text = "".join([cc.lower() for cc in text if cc.lower() in allowed_chars])
    lng = len(text)
    if lng == 0 or lng == 1:
        return True
    st_rg = range(lng // 2)
    en_rg = range(lng - 1, lng // 2 - 1 + lng % 2, -1)
    start = "".join([text[c] for c in st_rg])
    end_reversed = "".join([text[c] for c in en_rg])
    return start == end_reversed


if __name__ == "__main__":
    input = "A man, a plan, a canal: Panama"
    print(is_palindrome(input, ALLOWED_CHARS), input)
    input = "race a car"
    print(is_palindrome(input, ALLOWED_CHARS), input)
    input = " "
    print(is_palindrome(input, ALLOWED_CHARS), input)
    test_text = [
        "a",
        "aa",
        "ab",
        "aaa",
        "aab",
        "aba",
        "abb",
        "abc",
        "0",
        "00",
        "01",
        "000",
        "001",
        "010",
        "011",
        "012",
    ]
    for test_input in test_text:
        print(is_palindrome(test_input, ALLOWED_CHARS), test_input)
