#https://www.youtube.com/watch?v=UbyhOgBN834&t=291s
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        def same_permutation(a, b):
            d = collections.defaultdict(int)
            for x in a:
                d[x] += 1
            for x in b:
                d[x] -= 1
            return not any(d.values())
        
        # return same_permutation(s1,s2[0:3])
        
        l = len(s1)
        set1 = set(s1)
        for i in range(len(s2)-l + 1):
            if s2[i] in set1:
                if same_permutation(s1, s2[i:i+l]):
                    return True
            else:
                i = i + l
        return False
    
    

