# .rsplit() içerisine verilen parametreyi sağdan sola doğru ayırma işklemi yapar


metin = "simge karademir kartal istanbul"
sonuc = metin.rsplit(" ",2)
print(sonuc)

#--------------------------------------------------------------------------------------

# .splitlines() her bir alt satırdaki elemanların aralarına [,] karakteri ekler


metin = """
bilge
adam 
beşiktaş
yazılım
python
dersleri
"""

print(metin.splitlines())

# eğer parametre olarak sonuna true eklerseniz aralarına \n ekler

print(metin.splitlines(True))