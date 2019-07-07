


kaynak = "şçöğüıŞÇÖĞÜİ"
hedef = "scoguiSCOGUI"


ceviri_tablosu = str.maketrans(kaynak,hedef)
print(ceviri_tablosu)


metin = "bilge adam bireysel eğitimlerde artık python dersleri başlayacaktır"
print(metin)
metin = metin.translate(ceviri_tablosu)
print(metin)