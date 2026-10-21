class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded = encoded + str(len(string)) + "#" + string
        return encoded
    
    def decode(self, s: str) -> List[str]:
        string_list = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j]) #Finds the length between either start of string to # or between 2 #
            i = j+length+1
            string_list.append(s[j+1:i])
        return string_list
