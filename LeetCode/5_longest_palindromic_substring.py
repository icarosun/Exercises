class Solution:
    def longestPalindrome(self, s: str) -> str:
        bigger = (0, 0)
        for i in range(len(s)):
            odd = self.palindrome(i - 1, i + 1, s, len(s))

            even = self.palindrome(i, i + 1, s, len(s))

            if odd[1] - odd[0] > bigger[1] - bigger[0]:
                bigger = odd

            if even[1] - even[0] > bigger[1] - bigger[0]:
                bigger = even

        return s[bigger[0] : bigger[1] + 1]

    def palindrome(self, left, right, string, sizeString):
        while left >= 0 and right < sizeString and string[left] == string[right]:
            left -= 1
            right += 1

        return (left + 1, right - 1)
