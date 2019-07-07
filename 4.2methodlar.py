# .capitalize() => parametrede verilen değerin ilk harfini büyük olarak değiştirir

isim = "simge karademir".capitalize()

print(isim.capitalize())
print(isim.title())
# .title() isim içerisinde yer alan tüm ayrık kelimelerin ilk harfini büyük teslim eder

#------------------------------------------------------------------------------------------------

# .sorted() dizi içerisinde yer alan elelmanlerı a dna z ye , o dan 9 asıralama yapar


sonuc = sorted("bilgeadam")
print(sonuc)

# türkçe karakterleri dizinin en sonuna atar

import locale
#locale.setlocale(locale.LC_ALL,"Turkish_Turkey.1254")# windows için
#locale.setlocale(locale.LC_ALL,"tr_TR")# GNU\linux için

sonuc = sorted("bilgeadamöüçğ", key=locale.strxfrm)
print(sonuc)

#--------------------------------------------------------------------------------------------------

# .reverse() elinizde yer alan metni ya da dizi gibi nsnleri sıralama yapmadan tersine cevirir

sayilar = [1,2,3,4,5]
karakterler = ['a','b','c','d']
sayilar.reverse()
karakterler.reverse()
print(sayilar)
print(karakterler)

#----------------------------------------------------------------------------------------------------

# .split() içerisinde verilen parametreye göre soldan sağa doğru ayıtrma işlemi gerçekleştirir

elemanlar = "yazılım,sistem,teknik çizim,web grafik"
print(elemanlar)

elemanlar = elemanlar.split() #=> içerisine seperator olarak kullanıcağı parametre vermezseniz default olarak boşlukalrdan ayırır
print(elemanlar)

elemanlar = "yazılım,sistem,teknik çizim,web grafik"
elemanlar = elemanlar.split(",")
print(elemanlar)

#------------------------------------------------------------------------------------------------------------------------------------

# ex-1 dışardan girilien, metin içerisinde yer alan tüm karakterlerin ascii kod değerlerinin toplamını bulun


def metintoplamdeger(string):
    string = string.replace(" ","")
    havuz = 0
    liste = list(string)
    for i in liste:
        havuz += ord(i)
    return havuz
metin = input("lütfen metin giriniz : ")
result = metintoplamdeger(metin)
print(result)

#----------------------------------------------------------------------------------------------------------------------------------

metin = "murat vuranok yazılım beşiktaş istanbul"
sonuc = metin.split(" ",2)
print(sonuc)

















