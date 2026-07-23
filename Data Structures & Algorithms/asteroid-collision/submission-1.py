class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = [] # This is our "Safe Zone"

        for ast in asteroids: # Read the conveyor belt exactly once
            
            # The fight loop: Does the stack have an asteroid flying Right, 
            # while our new one is flying Left?
            while stack and stack[-1] > 0 and ast < 0:
                
                # Compare their sizes (just like your logic!)
                if stack[-1] == abs(ast):
                    stack.pop() # The one in the stack dies
                    break       # The new one dies too, so stop fighting
                    
                elif stack[-1] > abs(ast):
                    break       # The new one dies, stop fighting
                    
                else: 
                    stack.pop() # The one in the stack dies
                    # We DON'T break here. The new asteroid is still alive! 
                    # The while loop will spin again to fight the next guy in the stack.
            
            # This 'else' belongs to the 'while' loop. 
            # If the while loop finishes without hitting a 'break', 
            # it means the new asteroid survived all its fights!
            else:
                stack.append(ast)

        return stack