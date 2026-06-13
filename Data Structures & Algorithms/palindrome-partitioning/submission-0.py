class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(start, path):
            if start == len(s):
                res.append(path[:])
                return
            for i in range(start, len(s)):
                if is_palindrome(s, start, i):
                    path.append(s[start: i+1])
                    dfs(i+1, path)
                    path.pop()
        dfs(0,[])
        return res
            