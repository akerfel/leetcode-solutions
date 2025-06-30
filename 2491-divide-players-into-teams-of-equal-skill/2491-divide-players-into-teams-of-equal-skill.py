class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        sumSkill = sum(skill)
        team = sumSkill / (len(skill) / 2)
        counter = Counter(skill) 
        
        res = 0
        for i, player in enumerate(skill):
            friend = team - player
            if counter[friend] >= 1:
                counter[friend] -= 1
                res += friend * player
            else:
                return -1
        return res / 2