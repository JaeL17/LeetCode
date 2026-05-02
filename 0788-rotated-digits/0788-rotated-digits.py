class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        rotation = {'0': '0',
                    '1': '1',
                    '2': '5',
                    '5': '2',
                    '6': '9',
                    '8': '8',
                    '9': '6'}
        count = 0
        #good numer is differnt from x

        for i in range(n):
            temp_str = ''
            state = True
            for j in str(i+1):
                if j in rotation.keys():
                    temp_str += rotation[j]
                else:
                    state = False
                    break
            if state and temp_str != str(i+1):
                count +=1
                
        return count

        