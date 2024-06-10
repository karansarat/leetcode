class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        temp = path.split('/') 

        for i in temp:
            if i != '.' and i != '' and i != '..':
                stack.append(i)
            elif i == '..':
                if stack:
                    stack.pop()
        
        return '/' + '/'.join(stack)