# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ''
        curr_num = 0
        
        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)  
            elif char == '[':
                stack.append((curr_str, curr_num))
                curr_num = 0
                curr_str = ""
            elif char == ']':
                temp_str, temp_num = stack.pop()
                curr_str = temp_str + temp_num*curr_str
            else:
                curr_str +=char
        return curr_str
    
    
    