class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_set = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in anagram_set:
                anagram_set[sorted_word] = [word]
            else:
                anagram_set[sorted_word].append(word)
        return list(anagram_set.values())
#11:12 improved