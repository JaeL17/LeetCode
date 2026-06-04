class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness: int = 0
        
        # time complexity: O (n*m)
        for num in range(num1, num2 + 1):
            char = str(num)
            if len(char) >= 3: # the number is at least 3 digits
                for i in range(1, len(char)-1):
                    # check for peak
                    if (int(char[i]) > int(char[i-1]) and  int(char[i]) > int(char[i+1])) or (int(char[i]) < int(char[i-1]) and  int(char[i]) < int(char[i+1])):
                        waviness +=1
                    
        return waviness