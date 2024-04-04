# for each in "ankara ist".split(): # ret value = ["ankara","ist"]
#     print(each)

# liste = [8,2,3,4,5,6,7,1]

# summation = sum(liste)
# print(summation)

# i = 0
# while i < 4:
#     print(i)
#     i += 1

# len = len(liste)

# x = 0
# sum = 0
# while x < len:
#     sum += liste[x]
#     x += 1
# print(sum)

# # find min value
# liste = [8,2,3,4,5,6,7,1,0]
# min = liste[0]
# for each in liste:
#     if min > each:
#         min = each

# #print(min)

import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

print(array.shape) # 15 satir 1 sutunlu matris

matrix = array.reshape(3, 5) # 3 satir 5 sutuna ceviriyorum
print(matrix)

# dogrudan matris olusturma
array = np.array([
	[1,2,3,4,5],
	[6,7,8,9,10],
	[11,12,13,14,15]
])

print("shape: ", array.shape) # (3,5)
print("dimension: ", array.ndim) # matrisin boyutu

print("data type: ", array.dtype.name)
print("size: ", array.size) # eleman sayisi
print("type: ", type(array))

zeros = np.zeros((3, 4), dtype=np.int32)

print("zeros = ", zeros)
print("zeros data type = ", zeros.dtype.name)

np.ones((3, 4)) # 1 lerden olusan matris

empty = np.empty((3, 4))
print("empty = ", empty)

arange = np.arange(10, 50, 5) # 10,15,20,25,30,35,40,45 * 50 dahil değil
print(arange)

a2 = np.linspace(10, 50, 20) # 10 ile 50 arasını 20 parçaya bölüyo ve eşit aralıklarla dizi oluşturuyo

print(a2)


# numpy basic operations

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b) # satır ve sütunları ayrı ayrı topluyo kendi arasında ve toplanmış halini array olarak [5,7,9]

print(a - b) # üsttekinin aynısı

print(a ** 2) #her elemanın karesini alıyo

print(a + 2) # her elemana 2 ekliyo

print(np.sin(a)) #her elemanın sinüsünü alıyo

print(a < 2) # [True, False, False] döndürüyo her elemana ayrı ayrı kontrol

print(a * b) #her elemanı ayrı ayrı çarpıyo
print(a.dot(b.T)) # normal matris çarpımı

print(np.exp(a))

c = np.random.random((5,5))

print(c)
print(c.sum())
print(c.min())
print(c.max())