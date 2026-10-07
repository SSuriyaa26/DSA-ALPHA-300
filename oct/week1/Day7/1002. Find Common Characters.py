# leetcode Q1002

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        chars = {}
        for i in range(len(words[0])):
            chars[words[0][i]] = chars.get(words[0][i], 0) + 1 #init a hashmap with count of chars in 0th element
        for i in range(len(words)):
            current = {}#temp var
            for j in range(len(words[i])):
                current[words[i][j]] = current.get(words[i][j], 0) + 1 # count of current var
            for char in chars:
                if char not in current:
                    chars[char] = 0 # if element is not there then its set to 0
                elif current[char] < chars[char]:# find the min count between the 2
                    chars[char] = current[char]

        results = []
        #making the hashmap into list
        for char in chars:
            for j in range(chars[char]):
                results.append(char)
        return results

