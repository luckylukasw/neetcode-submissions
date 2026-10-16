class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_set = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in anagram_set:
                anagram_set[sorted_word] = [word]
            else:
                anagram_set[sorted_word].append(word)

        return_list = []
        for item_key in anagram_set:
            return_list.append(anagram_set[item_key])
        return return_list
#10:30