arr = [ 5,2,4,2,1,6,3 ]

def findDuplicate(arr):
    kuraKura = arr[0]
    kelinci = arr[arr[0]]
    while kuraKura != kelinci:
        kuraKura = arr[kuraKura]
        # print(kuraKura)
        kelinci = arr[arr[kelinci]]
        print(kelinci)
    kuraKura = 0
    while kuraKura != kelinci:
        kuraKura = arr[kuraKura]
        # print(kuraKura)
        kelinci = arr[kelinci]
        # print(kelinci)
    return kuraKura

findDuplicate(arr)