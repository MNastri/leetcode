"""Checks if a phrase is a palindrome."""
from string import ascii_lowercase


def is_palindrome(s):
    s = "".join([c.lower() for c in s if c.lower() in ascii_lowercase])
    print(s)


if __name__ == "__main__":
    input = "A man, a plan, a canal: Panama"
    is_palindrome(input)
    input = "race a car"
    is_palindrome(input)
    input = " "
    is_palindrome(input)
