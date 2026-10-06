class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        monotonically decreasing stack
        for every asteroid in the stack
        if positive, add to the stack
        if negative,
            - if smaller, keep popping until it hits something greater then v, keep popping until then
        stack = [2]
        2 4 -4 -1
        mono = 2
        top = 4
        """
        monostack = []
        for v in asteroids:
            while monostack and v < 0 and monostack[-1] > 0:
                if abs(v) > monostack[-1]:
                    monostack.pop()
                    continue
                elif monostack[-1] == abs(v):
                    monostack.pop()
                    break
                else:
                    break
            else:
                monostack.append(v)
        
        return monostack