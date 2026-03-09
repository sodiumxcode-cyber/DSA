#Leetcode-49 Group Anagrams
def GroupAnagrams(strs):
    group = {}

    for word in str:
        freq = {}
        for ch in word:
            freq[ch] = freq.get(ch, 0) + 1
        key = tuple(sorted(freq.items()))

        if key not in group:
            group[key] = []

        group[key].append(word)

    return list(group.values())