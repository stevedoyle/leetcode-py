# Title: Divide players into teams of equal skill
# URL: https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/
# Difficulty: Medium

from typing import List


class Solution:
    # Time complexity: O(nlogn)
    # Space complexity: O(1)
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        if n % 2 != 0:
            return -1
        num_teams = n // 2
        skill_sum = sum(skill)
        if skill_sum % num_teams != 0:
            return -1
        target = skill_sum // num_teams
        skill.sort()
        chemistry = 0
        for i in range(num_teams):
            team = [skill[i], skill[n - i - 1]]
            if sum(team) != target:
                return -1
            chemistry += self.chemistry(team)
        return chemistry

    def chemistry(self, team):
        product = 1
        for skill in team:
            product *= skill
        return product


class TestDividePlayers:
    def test_example1(self):
        skill = [3, 2, 5, 1, 3, 4]
        assert Solution().dividePlayers(skill) == 22

    def test_example2(self):
        skill = [3, 4]
        assert Solution().dividePlayers(skill) == 12

    def test_example3(self):
        skill = [1, 1, 2, 3]
        assert Solution().dividePlayers(skill) == -1
