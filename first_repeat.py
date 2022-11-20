# diberikan string str, buat function yang mengembalikan karakter pertama yang diulang. jika tidak ditemukan maka function tersebut mengembalikan nilai null

str = "kelelawar"

def find_doublechar(str):
    visited = {}
    for i in str:
        if visited.get(i):
            return i
        else:
            visited[i] = True
    return null

result = find_doublechar(str)

print(result)