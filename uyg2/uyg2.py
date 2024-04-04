"""
	* 
"""
#######################

lst = [1, 'abc', 3]

lst.append('xyz') # listeye eleman ekle
print(lst)

lst.clear() # listedeki elemanlari sil

print(lst)

#######################
lst = [1, 'abc', 3] 

del lst[:] # del lst[index] ile indexteki eleman siliniyor, [:] diyerek butun elemanlari sildim

########################
lst = [1, 'abc', 3]
lst2 = lst # shallow copy islemi yani ikisi de ayni listenin referansina sahip iki degisken oluyor

lst.append('xyz')

print(lst)
print(lst2) # referans tipli olduklari icin ve ikiside ayni referansa sahip oldugu icin herhangi biri degistiginde digeride ayni sekilde etkileniyo

lst3= lst.copy() # deep copy yaparak ayri referansli bir liste donduruyor
lst3.clear() # lst ve lst2 etkilenmedi
#######################

lst = [1,5,6,1,4] # lstye ayri bir referans atandi bu nedenle lst ve lst2 artik ayni listeyi isaret etmiyor

lst3 = lst[:] # bu da deep copy yapar yani ayni diziyi farkli bir referansla olusturuyor, lst deki degisiklikler lst3 u etkilemez tam tersi ayni sekilde

lst.append(15)
#######################

lst.count(3) # 3 degerinin liste icinde kac kez tekrar ettigini verir
#######################

lst.extend('xyz') # extend fonksiyonu parametredeki dizinin her elemanini tek tek diziye ekler 'xyz' bir karakter dizisi(string) oldugu icin 'x', 'y', 'z' olarak eklendi diziye

lst.extend([3,4,6]) # 3,4,6 tek tek eklenecek diziye

#######################

lst.insert(3, 5) # 3. indexten sonra 5 i ekliyor

lst4 = lst2[0:3:1]+ lst3 + lst[3:5:1] # toplama isareti ile de listeleri birlestirebiliyoruz

#######################

lst = [1, 3, 5, 6, 7, 8, 6, 10]

indexOfSix = lst.index(6) # 6 degeri listede varsa hangi indexte

indexOfSix2 = lst.index(6, indexOfSix + 1) # son bulunan indexten bir fazlasindan baslatarak varsa 2. tekrari ariyorum
    
#######################

# 6 nin lst icinde hangi indexlerde tekrarladigini bulan algoritmasi

yerler = []
yer = 0

lstLen = len(lst)

for i in range(yer, lstLen):
    print('loop counter =', i)
    try:
        yer = lst.index(6, yer) # 6 nin indexini al
        yerler.append(yer) # indexleri tuttugumuz diziye ekle
        yer += 1 # bir sonraki dongu icin yeri 1 arttir
        
    except: # 6 yi bulamadiginda buraya gelicek
        print('Index bulunamadi')
        break

print(yerler)

[i for i,el in enumerate(lst) if el == 6] # ustteki kodun tek satir hali

#######################

lastElem = lst.pop() # listenin son elemanini siliyo ve silinen elemani donduruyor deger olarak

lst.pop(3) # 3. indexi sil

#######################

lst1 = lst.copy().reverse() # lst nin ters cevrilmis kopyasi

#######################

lst.remove(1) # 1 degerinin bulundugu ilk elemani siler

#######################

lst = [1, 5, 6, 1, 4]
occurence = lst.count(1) # 1 kac kere tekrar ediyor
for i in range(occurence): # dizideki tum 1 leri sil
    lst.remove(1)

print(lst) # 1 ler silindi

#######################
