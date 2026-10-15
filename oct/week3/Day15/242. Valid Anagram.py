#leetcode Q49
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        words = {}

        for s in strs:
            chars = [0] * 26

            for char in s:
                chars[ord(char) - ord('a')] += 1

            key = tuple(chars)#use tuple since they are immutable and hashable

            if key not in words:
                words[key] = []

            words[key].append(s)

        return list(words.values())
