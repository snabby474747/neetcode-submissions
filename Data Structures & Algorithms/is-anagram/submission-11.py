class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # if len(s) != len(t):
        #     return False

        # setS,setT = {},{}

        # for i in range (len(s)):
        #     setS[s[i]]=1+setS.get(s[i],0)
        #     setT[t[i]]=1+setT.get(t[i],0)

        # for c in setS:
        #     if setS[c] != setT.get(c,0):
        #         return False
        
        # return True

        return Counter(s) == Counter(t) #shortcut solutions

        if len(s) != len(t):
            return False

        countS,countT = {},{}

        for i in range (len(s)):
            countS[s[i]] = 1+countS.get(s[i],0)
            countT[t[i]] = 1+countT.get(t[i],0)

        for c in countS:
            if countS[c] != countT.get(c,0):
                return False

        return True