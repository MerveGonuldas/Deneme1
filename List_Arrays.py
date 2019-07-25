# Sıralı, Değiştirilebilir özelliği var.. Aynı değeri birden fazla kez yazabiliyoruz(duplicate)
#indisler sıfırdan başlar
#[] köşe parantezler içinde yazılır.
#kopyalama özelliği var

ListeTipi=["elma","armut", "şeftali"]
print(ListeTipi)
print(len(ListeTipi))
print(ListeTipi[0])
print(ListeTipi[1])
print(ListeTipi[2])

ListeTipi[1]="karpuz" #1.indis armuttu. böylece onu karpuz yaptık.
print(ListeTipi)

ListeTipi.append("ananas")
print(ListeTipi)

ListeTipi.insert(1,"armut")
print(ListeTipi)

ListeTipi.remove("elma")
print(ListeTipi)

ListeTipi.pop() #içine indis numarasını/paramtresini girmezsek en son listeye aldığımızı kaldırır.
print(ListeTipi)

ListeTipi.pop(2)
print(ListeTipi)
print(ListeTipi[-1])

"""del ListeTipi[1] #dizinin elemanını siliyor.
print (ListeTipi)

del ListeTipi #dizinin tamamını siliyor.
print (ListeTipi) #hata verir. çünkü listeyi silmiş oluyoruz.

ListeTipi.clear()
print(ListeTipi)"""

yeniliste=ListeTipi.copy()
print("Kopyalanmış Liste")
print(yeniliste)

baskaliste=list(ListeTipi)
print(baskaliste)

for x in baskaliste:
    print(x) # veya print(baskaliste(x)) yazabiliriz.

if "muz" in baskaliste:
    print("Evet muz var.")
else:
    print("ürün bulunamadı")

sonliste=list(("Türkiye","Almanya","İsviçre"))
print(sonliste)

for ulke in sonliste:
    print(ulke)