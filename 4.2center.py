# .center() nesneye uygulandığında soldan sağdan eşit boşluklar verir
# metnin karakter uzunluğunu verilen değerden çıkartır ve kalandeğeri boşlk olarak sağa ve sola dağıtır


metin = "bilge adam"
print(len(metin))

metin = metin.center(15)
print(metin)
print(len(metin))