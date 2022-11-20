arr = [4,3,2,2,4,3,3]

def removeDuplicates(arr):
    visited = {}
    for element in arr:
        visited[element] = True
    return list(visited.keys())

print(removeDuplicates(arr))