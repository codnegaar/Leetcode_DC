class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False    
        number = x
        flipped = 0
        while number:
            flipped = flipped * 10 + number % 10
            number //= 10
        return x == flipped
