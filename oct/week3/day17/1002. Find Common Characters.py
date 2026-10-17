#leetcode Q1002
class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        chars = {}
        for i in range(len(words[0])):
            chars[words[0][i]] = chars.get(words[0][i], 0) + 1
        for i in range(len(words)):
            current = {}
            for j in range(len(words[i])):
                current[words[i][j]] = current.get(words[i][j], 0) + 1
            for char in chars:
                if char not in current:
                    chars[char] = 0
                elif current[char] < chars[char]:
                    chars[char] = current[char]

        results = []
        for char in chars:
            for j in range(chars[char]):
                results.append(char)
        return results    

