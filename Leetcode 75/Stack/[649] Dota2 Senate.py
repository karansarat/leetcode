class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        n = len(senate)

        rad = [i for i in range(len(senate)) if senate[i]=='R']
        dire = [j for j in range(len(senate)) if senate[j]=='D']
        
        while rad and dire:
            r = rad.pop(0)
            d = dire.pop(0)
            if r < d:
                rad.append(n + r)
            else:
                dire.append(n + d)
                
        return 'Radiant' if rad else 'Dire'