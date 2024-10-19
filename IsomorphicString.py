class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dic={}
        for i,j in zip(s,t):
            dic[i]=j
        if len(set(dic.values()))!=len(dic.values()):
            return False
        x=""
        for i in s:
            x+=dic[i] #Humko T ke saath equal karna hai
        if x==t:
            return True
        else:
            return False