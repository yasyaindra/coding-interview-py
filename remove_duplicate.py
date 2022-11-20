arr = [2,2,2,2,2,2,2]

def removeDuplicates(arr):
    new = []
    for i in arr:
        if i not in new:
            new.append(i)
    return new

print(removeDuplicates(arr))