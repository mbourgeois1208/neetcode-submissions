class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        more = True 

        while more:
            for i in range(len(asteroids)-1):
                if asteroids[i]>0 and asteroids[i+1]<0:
                    more = True 
                    if asteroids[i] == abs(asteroids[i+1]): 
                        del asteroids[i:i+2]
                        break
                    elif asteroids[i] > abs(asteroids[i+1]):
                        del asteroids[i+1]
                        break
                    else: 
                        del asteroids[i]
                        break
            else: more = False 

        
        return asteroids


            