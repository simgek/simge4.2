# endswith() metnin parametrede gçndrdiğiniz değer ile bitip bitmediğini size true false olarak teslim eder

metin = "simge karademir"

sonuc = metin.endswith("or")
print("metin or kelimesi ile bitmektedir") if sonuc else print("metin or kelimesiyle bitmemektedir")


# ex-1 kaç tane .png var

file1  = "ba.png"
file2  = "ba.jpg"
file3  = "ba.gif"
file4  = "ba.png"
file5  = "ba.tff"
file6  = "ba.mp3"
file7  = "ba.mp4"
file8  = "ba.jpg"
file9  = "ba.gif"
file10 = "ba.png"
file11 = "ba.gif"

toplam = 0
for i in file1,file2,file3,file4,file5,file6,file7,file8,file9,file10,file11:
    result = i.endswith(".png")
    if result:
        toplam += 1
        print(i)

print(toplam)


# metot
def kontrolet(*param):
    toplam = 0
    for i in param:
        result = i.endswith(".png")
        if result:
            toplam += 1
    return toplam
result = kontrolet(file1,file2,file3,file4,file5,file6,file7,file8,file9,file10,file11)
print(result)