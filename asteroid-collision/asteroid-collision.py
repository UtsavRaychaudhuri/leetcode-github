class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids)<=1:
            return asteroids
        stack=[]
        for i in asteroids:
            if i<0 and len(stack)>0 and stack[-1]>0:
                if abs(stack[-1])==-i:
                    stack.pop()
                    continue
                while(stack):
                    if stack[-1]>0 and stack[-1]>abs(i):
                        break
                    elif stack[-1]>0 and stack[-1]<abs(i):
                        stack.pop()
                        if len(stack)==0:
                            stack.append(i)
                            break
                    elif stack[-1]>0 and stack[-1]==abs(i):
                        stack.pop()
                        break
                    else:
                        stack.append(i)
                        break
            else:
                stack.append(i)
        return stack
                
                
            