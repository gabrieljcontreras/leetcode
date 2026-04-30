class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*', '/']
        res = []
        num = 0
        for i in tokens: 
            if i not in ops: 
                res.append(int(i))
            else: 
                b = res.pop()
                a = res.pop()
                if i == '+': 
                    num = a + b
                    res.append(int(num))
                elif i == '-': 
                    num = a - b
                    res.append(int(num))
                elif i == '*': 
                    num = a * b
                    res.append(int(num))
                elif i == "/":
                    num = a / b
                    res.append(int(num))
        return res[0]
