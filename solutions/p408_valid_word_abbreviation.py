class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # Split the abbreviation into parts - letters and numbers
        parts = []
        i = 0
        while i < len(abbr):
            if abbr[i].isdigit():
                if abbr[i] == "0":
                    # Leading zero is not allowed
                    return False
                num_start = i
                while i < len(abbr) and abbr[i].isdigit():
                    i += 1
                parts.append(abbr[num_start:i])
            else:
                parts.append(abbr[i])
                i += 1

        # Now we have a list of parts, we need to check if they can form the word
        i = 0
        for part in parts:
            if part.isdigit():
                # If it's a number, we need to skip that many characters in the word
                skip = int(part)
                print(skip)
                i += skip
            else:
                # If it's a letter, we need to check if it matches the word
                if i >= len(word) or word[i] != part:
                    return False
                i += 1
        # After processing all parts, we should have consumed the entire word
        return i == len(word)


class TestValidWordAbbreviation:
    def test_example1(self):
        word = "internationalization"
        abbr = "i12iz4n"
        expected = True
        sol = Solution()
        result = sol.validWordAbbreviation(word, abbr)
        assert result == expected

    def test_example2(self):
        word = "apple"
        abbr = "a2e"
        expected = False
        sol = Solution()
        result = sol.validWordAbbreviation(word, abbr)
        assert result == expected

    def test_example3(self):
        word = "word"
        abbr = "w1r"
        expected = False
        sol = Solution()
        result = sol.validWordAbbreviation(word, abbr)
        assert result == expected

    def test_example4(self):
        word = "abbde"
        abbr = "a1b01e"
        expected = False
        sol = Solution()
        result = sol.validWordAbbreviation(word, abbr)
        assert result == expected
