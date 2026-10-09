#leetcode Q345
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u'] #vowels array
        l = 0
        r = len(s) - 1
        letters = list(s)
        while l < r:
            while letters[r].lower() not in vowels and l < r:
                r -= 1
            while letters[l].lower() not in vowels and l < r:
                l += 1

            letters[l], letters[r] = letters[r], letters[l]
            r -= 1
            l += 1

        result = "".join(letters)
        return result

