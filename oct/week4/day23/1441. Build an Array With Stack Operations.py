#leetcode Q1441
class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        stack = []
        res = []#store operations
        top1 = 0#stack pointer
        top2 = 0#target pointer

        for i in range(1, n + 1):
            stack.append(i)
            top1 += 1
            res.append("Push")

            if i != target[top2]:
                stack.pop()
                top1 -= 1
                res.append("Pop")
            else:
                top2 += 1

            if top2 == len(target):
                break

        return res