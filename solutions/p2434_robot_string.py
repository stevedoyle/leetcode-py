from collections import Counter


class Solution:
    def robotWithString(self, s: str) -> str:
        dic, t, ans = Counter(s), [], []
        for char in s:
            t.append(char)
            if dic[char] == 1:
                del dic[char]
            else:
                dic[char] -= 1
            while dic and t and min(dic) >= t[-1]:
                ans += t.pop()
        ans += t[::-1]
        return "".join(ans)


class TestRobotWithString:
    def test_example1(self):
        assert Solution().robotWithString("zza") == "azz"

    def test_example2(self):
        assert Solution().robotWithString("bac") == "abc"

    def test_example3(self):
        assert Solution().robotWithString("bdda") == "addb"
