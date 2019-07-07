# .count() metin ya da dizi içerisinde parametrede verilen değerin adet bilgisini teslim eder

metin = "bilge adam beşiktaş"
sonuc = metin.count("b")
print("metin içerisinde toplamda verdiğiniz parametre {} adet içermektedir".format(sonuc))



metinler = ["ankara","edirne","istanbul","ankara","eskişehir"]
result = metinler.count("ankara")
print(result)


metin = "simge karademir"
sonuc = metin.count("a")
print(sonuc)
sonuc = metin.count("a",2) # arama işlemine 2. indexten başlar


metin = "bilge adam beşiktaş"
sonuc = metin.count("a")
print("toplam a karakteri {} tanedir".format(sonuc))

sonuc = metin.count("a",1,2) # a karakterini 0. ,ndexten 2. indexe kadar ara
print("toplam a karakteri {} tanedir".format(sonuc))