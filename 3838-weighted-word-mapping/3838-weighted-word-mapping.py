class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        answer : str = ""
        mod: int = 26
        alpabhet = 'abcdefghijklmnopqrstuvwxyz'
        weights_dict: dict[str, int] ={}
        num_to_alp: dict[int, str] = {}

        for alp, weight in zip(alpabhet, weights):
            weights_dict[alp] = weight
        
        for i in range(len(alpabhet)):
            num_to_alp[25-i] = alpabhet[i]

        for word in words:
            temp_weight = 0
            for char in word:
                temp_weight += weights_dict[char]
            answer += num_to_alp[temp_weight%26]

        return answer




        