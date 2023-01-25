class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill)-1
        count = 0
        target = skill[-1] + skill[0]
        sum_ = 0
        while l<r:
            if skill[r] + skill[l]==target:
                count +=1
                sum_ += skill[r] * skill[l]
            r-=1
            l+=1
        if len(skill)//2==count:
            return sum_
        return -1
