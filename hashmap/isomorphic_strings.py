freq = {}
s = 'abb'
t = 'eff'
for i in s:
    freq[i] = freq.get(i, 0) + 1
        
for i in t:
    freq[i] = freq.get(i, 0) + 1

print(freq)
        
def add(nums, num):
    return nums + num


def sub(nums, num):
    return nums - num

def mult(nums, num):
    nums * num

def div(nums, num):
    nums / num

nums = [1, 2, 3, 4, 5, 6]
for i in range(0, nums):
    if i < len(nums):
        print(True)
    else:
        print(False)