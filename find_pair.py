
arr = [1,3,5,6,9]
k = 12
def find_pair(arr, k):
    visited = {}
    for element in arr: 
        if visited.get(k-element):
            return True 
        else:
            visited[element] = True
    return False

result = find_pair(arr, k)
result_2 = find_pair(arr, 32)

print(result) 
print(result_2) 
# True
# False