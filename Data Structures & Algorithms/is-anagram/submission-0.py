class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for letter in s:
            if letter not in counts:
                counts[letter] = 1
            else:
                counts[letter] += 1
        for letter in t:
            if letter not in counts:
                return False
            counts[letter] -= 1
            if counts[letter] < 0:
                return False
            if counts[letter] == 0:
                del counts[letter]
        
        return len(counts.keys()) == 0
