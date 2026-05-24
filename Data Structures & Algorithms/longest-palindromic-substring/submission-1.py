class Solution:
    def longestPalindrome(self, s: str) -> str:
        pair = [0, 0]

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # left+1 and right-1 are the last valid bounds
            return right - left - 2, left + 1, right - 1

        for i in range(len(s)):
            # Odd length palindrome (center at i)
            length1, l1, r1 = expand(i, i)
            # Even length palindrome (center between i and i+1)
            length2, l2, r2 = expand(i, i + 1)

            if length1 > length2 and length1 > pair[1] - pair[0]:
                pair = [l1, r1]
            elif length2 >= length1 and length2 > pair[1] - pair[0]:
                pair = [l2, r2]

        return s[pair[0]:pair[1] + 1]