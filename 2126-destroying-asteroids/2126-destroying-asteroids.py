class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        
        # O(n) time complexity, O(1) space complexity
        asteroids.sort() 
        for asteroid in asteroids:
            if mass < asteroid:
                return False
            
            mass += asteroid

        return True