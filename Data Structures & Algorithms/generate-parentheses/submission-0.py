class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtracking(current, open_left, close_left):
            if open_left == 0 and close_left == 0:
                res.append(current)
                return
            if open_left > 0:
                backtracking(current + "(", open_left - 1, close_left)
            if close_left > open_left: 
                backtracking(current + ")", open_left, close_left -1)
        backtracking("", n, n)
        return res
            