#Leetcode-1189 maximum num of balloons
def maxBalloon(text):
    freq = {}
    for i in text:
        freq[i] = freq.get(i, 0) + 1
    
    balloon = "balloon"
    maxballoon = float('inf')

    maxFreq = {}
    for i in balloon:
        maxFreq[i] = maxFreq.get(i, 0) + 1

    for key, count in maxFreq.items():
        maxballoon = min(maxballoon, freq.get(key, 0) // count)
    return 0 if maxballoon == float('inf') else maxballoon