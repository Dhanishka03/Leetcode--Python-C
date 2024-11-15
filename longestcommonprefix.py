class Solution(object):
    def longestCommonPrefix(self, strs):
    # Start with the first string as the common prefix
        prefix = strs[0]
    
    # Compare the prefix with each string
        for s in strs[1:]:
        # Shorten the prefix until it matches the start of s
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
    
        return prefix
        
