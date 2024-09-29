# Title: All O`one Data Structure
# URL: https://leetcode.com/problems/all-oone-data-structure/
# Difficulty: Hard


class AllOne:
    def __init__(self):
        self.counts = {}
        self.freqs = {}

    def freq_set(self, count, key):
        if count not in self.freqs:
            self.freqs[count] = []
        self.freqs[count].append(key)

    def freq_clear(self, count, key):
        self.freqs[count].remove(key)
        if len(self.freqs[count]) == 0:
            del self.freqs[count]

    def inc(self, key: str) -> None:
        if key in self.counts:
            self.counts[key] += 1
            self.freq_set(self.counts[key], key)
            self.freq_clear(self.counts[key] - 1, key)
        else:
            self.counts[key] = 1
            self.freq_set(1, key)

    def dec(self, key: str) -> None:
        if key in self.counts:
            self.counts[key] -= 1
            if self.counts[key] == 0:
                del self.counts[key]
                self.freq_clear(1, key)
            else:
                if self.counts[key] not in self.freqs:
                    self.freqs[self.counts[key]] = []
                self.freq_set(self.counts[key], key)
                self.freq_clear(self.counts[key] + 1, key)

    def getMaxKey(self) -> str:
        max_count = max(self.freqs) if self.freqs else 0
        if max_count > 0:
            if len(self.freqs[max_count]) > 0:
                return self.freqs[max_count][0]
        return ""

    def getMinKey(self) -> str:
        min_count = min(self.freqs) if self.freqs else 0
        if min_count > 0:
            if len(self.freqs[min_count]) > 0:
                return self.freqs[min_count][0]
        return ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()


class TestAllOne:
    def test_example1(self):
        obj = AllOne()
        obj.inc("hello")
        obj.inc("hello")
        assert obj.getMaxKey() == "hello"
        assert obj.getMinKey() == "hello"
        obj.inc("leet")
        assert obj.getMaxKey() == "hello"
        assert obj.getMinKey() == "leet"

    def test_example2(self):
        obj = AllOne()
        obj.inc("hello")
        obj.inc("hello")
        obj.dec("hello")
        assert obj.getMaxKey() == "hello"
        assert obj.getMinKey() == "hello"
        obj.dec("hello")
        assert obj.getMaxKey() == ""
        assert obj.getMinKey() == ""
