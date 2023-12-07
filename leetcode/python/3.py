## Leetcode Problem 3 - Longest Substring Without Repeating Characters
## Dec. 7, 2023

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        ans, start = 0, 0
        for end in range(len(s)):
            if s[end] in visited:
                start = max(start, visited[s[end]] + 1)
            visited[s[end]] = end
            ans = max(ans, end - start + 1)
        return ans

    def lengthOfLongestSubstring1(self, s: str) -> int:
        ans, temp = 0, ''
        for i in s:
            while i in temp:
                temp = temp[1:]
            temp += i
            ans = max(ans, len(temp))
        return ans