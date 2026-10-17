class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result
    def decode(self, result: str) -> List[str]:
        res = []
        i=0
        while i<len(result):
            j = i
            while result[j] != "#":
                j+=1
            length = int(result[i:j])
            start = j+1
            end = start + length 
            res.append(result[start:end])
            i = end
        return res    
