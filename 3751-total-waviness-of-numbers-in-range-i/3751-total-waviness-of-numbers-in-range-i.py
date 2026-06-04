class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness: int = 0
        
        for num in range(num1, num2 + 1):

            if num > 100: # the number is at least 3 digits
                char = str(num)
                for i in range(1, len(char)-1):
                    # if i - 1 > 0 and i + 1 < len(char):

                    # check for peak
                    if int(char[i]) > int(char[i-1]) and  int(char[i]) > int(char[i+1]):
                        waviness +=1
                    
                    # check for valley
                    elif int(char[i]) < int(char[i-1]) and  int(char[i]) < int(char[i+1]):
                        waviness +=1

        return waviness