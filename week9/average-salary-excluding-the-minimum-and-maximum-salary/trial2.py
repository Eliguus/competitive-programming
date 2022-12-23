class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary_sum=sum(salary)
        salary_sum-=(salary[0]+salary[-1])
        ave=salary_sum/(len(salary)-2)
        return ave
