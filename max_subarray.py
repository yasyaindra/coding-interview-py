arr = [1,-3,5,7]

def maxSumSubarray(arr):
    globalSum = float("-inf")
    localSum = 0
    for element in arr:
        localSum = max(element, localSum+element)
        globalSum = max(globalSum, localSum)
    return globalSum

# result = maxSumSubarray(arr)
maxSumSubarray(arr)

# print(result)