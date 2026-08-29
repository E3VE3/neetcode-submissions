class Solution:
    def isPalindrome(self, s: str) -> bool:
        palin = "".join(char for char in s if char.isalnum()).casefold()
        return palin == palin[::-1]
