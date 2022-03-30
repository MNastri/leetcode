"""Checks if a phrase is a palindrome."""
from string import ascii_lowercase


def is_palindrome(s) -> bool:
    s = "".join([c.lower() for c in s if c.lower() in ascii_lowercase])
    l = len(s)
    if l == 0 or l == 1:
        return True
    # print(s)


if __name__ == "__main__":
    input = "A man, a plan, a canal: Panama"
    print(is_palindrome(input))
    input = "race a car"
    print(is_palindrome(input))
    input = " "
    print(is_palindrome(input))
