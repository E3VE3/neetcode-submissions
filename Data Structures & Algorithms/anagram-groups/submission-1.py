class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            ananams = defaultdict(list)

            for word in strs:
                ananams[str(sorted(word))].append(word)
            return list(ananams.values())
                
        
        