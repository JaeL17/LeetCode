class Solution:
    def numberToWords(self, num: int) -> str:
        # Unique english representation with no rule
        zero_to_nineteen: List[str] = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        twenty_to_ninty: List[str] = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        after_hundred: List[str] = ["Hundred", "Thousand", "Million", "Billion"]

        if num < 20:
            return zero_to_nineteen[num]

        elif num < 100:
            # print(num)
            return (twenty_to_ninty[(num // 10 ) - 2] + " " + (self.numberToWords(num % 10) if num % 10 else "")).strip()
  
        elif num < 1000: # thousdand
            # e.g. 957 -> Nine Hundred Fifty Seven
            return (self.numberToWords(num // 100 ) + " " + after_hundred[0] + " " + (self.numberToWords(num % 100) if num % 100 else "")).strip()
        
        # after this point after_hundred index increase by one for every 1000 factor. and the number for opertaion also increases by # 1000 factor. 
        for i in range(1, len(after_hundred)):
            val = 1000 ** i
            if num < val * 1000:
                return (self.numberToWords(num // val ) + " " + after_hundred[i] + " " + (self.numberToWords(num % val) if num % val else "")).strip()

        # elif num < 1_000_000: # million
        #     # e.g. 123957 -> One Hundred Twenty Three Thousand Nine Hundred Fifty Seven
        #     return (self.numberToWords(num // 1000 ) + " " + after_hundred[1] + " " + (self.numberToWords(num % 1000) if num % 1000 else "")).strip()
        
        # elif num < 1_000_000_000: # Billion

        #     return ((self.numberToWords(num // 1_000_000 ) + " " + after_hundred[2] + " " + (self.numberToWords(num % 1_000_000) if num % 1_000_000 else ""))).strip()
        # else:
        #     return ((self.numberToWords(num // 1_000_000_000 ) + " " + after_hundred[3] + " " + (self.numberToWords(num % 1_000_000_000) if num % 1_000_000_000 else ""))).strip()

        