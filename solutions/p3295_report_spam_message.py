# Title: Report Spam Message
# URL: https://leetcode.com/problems/report-spam-message/
# Difficulty: Medium

from typing import List


class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        banned = set(bannedWords)
        count = 0
        for word in message:
            if word in banned:
                count += 1
                if count == 2:
                    return True
        return False


class TestReportSpam:
    def test_example1(self):
        input = ["hello", "world", "leetcode"]
        bannedWords = ["world", "hello"]
        assert Solution().reportSpam(input, bannedWords)

    def test_example2(self):
        input = ["hello", "programming", "fun"]
        bannedWords = ["world", "programming", "leetcode"]
        assert not Solution().reportSpam(input, bannedWords)
