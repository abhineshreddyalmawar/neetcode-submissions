class Solution:
    def groupAnagrams(self, strs : list[str]) -> list[list[str]]:
        groups={} # created the dict for storing the keu:value for similar groups
        for word in strs: # looping thru "act","pots","tops","cat","stop","hat"
            key = "".join(sorted(word)) # keys are act,opst,aht
            if key in groups: # if act,opst,aht in groups:
                groups[key].append(word) # groups:{"act":["cat"], "opst":["stop", "tops""], "aht": ["hat"]}
            else:
                groups[key]=[word] # groups:{"act":["cat"]
        return list(groups.values()) # returns list of values:[["hat"],["act", "cat"],["stop", "pots", "tops"]]
print(Solution().groupAnagrams(["act","pots","tops","cat","stop","hat"]))
print(Solution().groupAnagrams(["x"]))
print(Solution().groupAnagrams([""]))