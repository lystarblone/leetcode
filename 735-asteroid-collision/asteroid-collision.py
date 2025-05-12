class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        output=[]
        for i in asteroids:
            while output and i<0 and output[-1]>0:
                if abs(i)>abs(output[-1]):
                    output.pop()
                    continue
                elif abs(i)==abs(output[-1]):
                    output.pop()
                break
            else:
                output.append(i)
        return output