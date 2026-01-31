#Leetcode-242 Valid Anagrams
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if ch not in freq:
            return False

        freq[ch] -= 1
        if freq[ch] == 0:
            del freq[ch]
    return len(freq) == 0