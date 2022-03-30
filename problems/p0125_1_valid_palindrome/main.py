"""Checks if a phrase is a palindrome."""
from string import ascii_lowercase


def is_palindrome(text: str) -> bool:
    text = "".join([cc.lower() for cc in text if cc.lower() in ascii_lowercase])
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
    print(is_palindrome(input))
    input = "race a car"
    print(is_palindrome(input))
    input = " "
    print(is_palindrome(input))
