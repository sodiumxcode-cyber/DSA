#Leetcode-383 Ransom Note
def ransomNote(ransome, magazine):
    freq = {}
    for i in magazine:
        freq[i] = freq.get(i, 0) + 1
    
    for i in ransome:
        if i not in freq or freq[i] == 0:
            return False
        freq[i] -= 1
    return True