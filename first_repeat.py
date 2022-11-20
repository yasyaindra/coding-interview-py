# diberikan string str, buat function yang mengembalikan karakter pertama yang diulang. jika tidak ditemukan maka function tersebut mengembalikan nilai null

str = "kuda"

def find_doublechar(str):
    visited = {}
    for i in str:
        if visited.get(i):
            return i
        else:
            visited[i] = True
    return '\0'

result = find_doublechar(str)

print(result)