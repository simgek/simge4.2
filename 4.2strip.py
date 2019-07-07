# .strip() metin başındakiveya sonudaki karakterleri silmek için kullanılır

metin = " bilge adam "
print(metin)
print(len(metin))

metin = metin.strip(" ") # soladki ve sağdaki boşlukları siler
print(metin)
print(len(metin))

metin= " bilge adam "
metin = metin.lstrip() # soldaki boşluğu siler
print(len(metin))

metin= " bilge adam "
metin = metin.rstrip() # sağdaki boşluğu siler
print(len(metin))