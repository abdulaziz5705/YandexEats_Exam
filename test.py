class Solution:
    def isPalindrome(self, x: int) -> bool:
        negative = x < 0
        x = abs(x)
        x = int(str(x)[::-1])
        if negative:
            x = -x
            if x < (x % 10) * 100 + (x // 10) % 10 * 10 + x // 100 or x > (
                    (x % 10) * 100 + (x // 10) % 10 * 10 + x // 100):
                return False
        return True


