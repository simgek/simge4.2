# .find() .rfind()



metin = "murat vuranok bilge adam beşiktaş yazılım"
sonuc = metin.find("a") # verilen karakterin metin içerisnde soldan sağa doğru
# arama işlemi yapar eğer belirtilem karakter metin içerisinde var ise
# index değereini yok ise hata
print(sonuc)



sonuc = metin.rfind("a") # verilen karakterin metin içerisnde sağdan sola doğru
# arama işlemi yapar eğer belirtilem karakter metin içerisinde var ise
# index değereini yok ise hata
print(sonuc)