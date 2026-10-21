class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_chunks = []
        for string in strs:
            encoded_chunks.append(f"{len(string)}#{string}")
        return "".join(encoded_chunks)
    
    def decode(self, s: str) -> List[str]:
        string_list = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j]) #Finds the length between either start of string to # or between 2 #
            i = j+length+1
            string_list.append(s[j+1:i])
        return string_list
