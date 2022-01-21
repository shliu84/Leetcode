#https://www.youtube.com/watch?v=6DUA6FNJP1I
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        res = []
        for w in words:
            res.append(w[::-1])
            res.append(" ")
        
        
        return "".join(res).strip()