class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for asteroid in asteroids:
            # While the current asteroid can collide with a right-bound asteroid
            while stk and stk[-1] > 0 and asteroid < 0:
                if abs(asteroid) < abs(stk[-1]):
                    break
                elif abs(asteroid) == abs(stk[-1]):
                    stk.pop()
                    break
                elif abs(asteroid) > abs(stk[-1]):
                    stk.pop()
                    continue
            else:
                stk.append(asteroid)
        
        return stk
                