class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, max_length = 0, 0, 0
        window = set()

        while right < len(s):
            while s[right] in window:
                window.discard(s[left])
                left += 1

            max_length = max(max_length, right - left + 1)
            window.add(s[right])
            right += 1

        return max_length
