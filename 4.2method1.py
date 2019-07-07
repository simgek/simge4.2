#dışardan gelicek parametre sayısı belirsiz olan durumlarda kullanılır

def hesapla(*sayilar):
    toplam = 0
    for i in sayilar:
        toplam += i
    return toplam
result = hesapla(1,2,3,4,5,6,7,8,9)
print(result)

