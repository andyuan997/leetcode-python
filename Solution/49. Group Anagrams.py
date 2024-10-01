class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]

        hash_table = {}

        for s in strs:
            sorted_str = ''.join(sorted(s))

            if sorted_str in hash_table:
                hash_table[sorted_str].append(s)
            else:
                hash_table[sorted_str] = [s]

        return list(hash_table.values())
